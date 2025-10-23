# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class IssueBadgeSettings(models.Model):
    _name = 'issuebadge.settings'
    _description = 'IssueBadge API Settings'
    _rec_name = 'company_id'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company,
        help='Company for which this API configuration applies'
    )
    api_key = fields.Char(
        string='IssueBadge API Key',
        required=True,
        help='Bearer token from https://app.issuebadge.com/developer'
    )
    api_url = fields.Char(
        string='API Base URL',
        default='https://app.issuebadge.com/api/v1',
        required=True,
        help='IssueBadge API endpoint URL'
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )
    last_sync_date = fields.Datetime(
        string='Last Badge Sync',
        readonly=True,
        help='Last time badges were synced from API'
    )

    _sql_constraints = [
        ('company_unique', 'unique(company_id)',
         'Only one API configuration per company is allowed!')
    ]

    def action_test_connection(self):
        """Test the API connection"""
        self.ensure_one()

        import requests

        try:
            response = requests.post(
                f'{self.api_url}/validate-key',
                headers={
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            if data.get('success'):
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Connection Successful!',
                        'message': f"Connected as: {data.get('user', {}).get('name', 'Unknown')}",
                        'type': 'success',
                        'sticky': False,
                    }
                }
            else:
                raise UserError('API key validation failed. Please check your credentials.')

        except requests.exceptions.RequestException as e:
            raise UserError(f'Connection failed: {str(e)}')

    def action_sync_badges(self):
        """Sync badges from API"""
        self.ensure_one()

        badge_obj = self.env['issuebadge.badge']
        synced_count = badge_obj.sync_badges_from_api()

        self.last_sync_date = fields.Datetime.now()

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Badges Synced!',
                'message': f'Successfully synced {synced_count} badge(s)',
                'type': 'success',
                'sticky': False,
            }
        }
