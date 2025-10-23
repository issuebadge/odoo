# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
import logging

_logger = logging.getLogger(__name__)


class IssueBadgeBadge(models.Model):
    _name = 'issuebadge.badge'
    _description = 'Badge Templates'
    _order = 'name'

    name = fields.Char(
        string='Badge Name',
        required=True,
        help='Name of the badge template'
    )
    badge_id = fields.Char(
        string='Badge ID',
        required=True,
        help='Unique identifier from IssueBadge'
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True
    )
    issue_count = fields.Integer(
        string='Times Issued',
        default=0,
        readonly=True,
        help='Number of times this badge has been issued'
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )
    last_issued_date = fields.Datetime(
        string='Last Issued',
        readonly=True
    )

    _sql_constraints = [
        ('badge_id_company_unique', 'unique(badge_id, company_id)',
         'This badge already exists for this company!')
    ]

    @api.model
    def sync_badges_from_api(self):
        """Fetch badges from IssueBadge API and sync to Odoo"""
        settings = self.env['issuebadge.settings'].search([
            ('company_id', '=', self.env.company.id),
            ('active', '=', True)
        ], limit=1)

        if not settings:
            raise UserError(
                'Please configure IssueBadge API settings first.\n'
                'Go to IssueBadge > Configuration > Settings'
            )

        try:
            response = requests.get(
                f'{settings.api_url}/badge/getall',
                headers={
                    'Authorization': f'Bearer {settings.api_key}',
                    'Content-Type': 'application/json'
                },
                timeout=30
            )
            response.raise_for_status()
            data = response.json()

            if not data.get('success'):
                raise UserError('API returned an error. Please check your settings.')

            badge_data_list = data.get('data', [])
            synced_count = 0

            for badge_data in badge_data_list:
                badge_id = badge_data.get('id')
                badge_name = badge_data.get('name')

                if not badge_id or not badge_name:
                    continue

                existing = self.search([
                    ('badge_id', '=', badge_id),
                    ('company_id', '=', self.env.company.id)
                ], limit=1)

                if existing:
                    # Update existing badge name if changed
                    if existing.name != badge_name:
                        existing.name = badge_name
                        _logger.info(f'Updated badge: {badge_name}')
                else:
                    # Create new badge
                    self.create({
                        'name': badge_name,
                        'badge_id': badge_id,
                        'company_id': self.env.company.id
                    })
                    _logger.info(f'Created badge: {badge_name}')
                    synced_count += 1

            return synced_count

        except requests.exceptions.RequestException as e:
            _logger.error(f'Error syncing badges: {str(e)}')
            raise UserError(f'Failed to sync badges from API:\n{str(e)}')
        except Exception as e:
            _logger.error(f'Unexpected error: {str(e)}')
            raise UserError(f'An unexpected error occurred:\n{str(e)}')

    def action_issue_badge(self):
        """Open wizard to issue this badge"""
        self.ensure_one()

        return {
            'name': 'Issue Badge',
            'type': 'ir.actions.act_window',
            'res_model': 'issuebadge.send.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_badge_id': self.id,
            }
        }

    def action_view_issued_badges(self):
        """View all badges issued from this template"""
        self.ensure_one()

        return {
            'name': f'Issued: {self.name}',
            'type': 'ir.actions.act_window',
            'res_model': 'issuebadge.issue',
            'view_mode': 'tree,form',
            'domain': [('badge_id', '=', self.id)],
            'context': {'create': False}
        }
