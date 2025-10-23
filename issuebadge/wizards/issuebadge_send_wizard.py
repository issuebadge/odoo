# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
import uuid
import logging

_logger = logging.getLogger(__name__)


class IssueBadgeSendWizard(models.TransientModel):
    _name = 'issuebadge.send.wizard'
    _description = 'Send Badge Wizard'

    badge_id = fields.Many2one(
        'issuebadge.badge',
        string='Badge Template',
        required=True,
        domain=[('active', '=', True)],
        help='Select the badge template to issue'
    )
    recipient_name = fields.Char(
        string='Recipient Name',
        required=True,
        help='Full name of the badge recipient'
    )
    recipient_email = fields.Char(
        string='Recipient Email',
        help='Email address (optional, but recommended for notifications)'
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Select from Contacts',
        help='Choose an existing contact to auto-fill name and email'
    )
    notes = fields.Text(
        string='Notes',
        help='Optional notes about this badge issuance'
    )

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        """Auto-fill recipient details from selected partner"""
        if self.partner_id:
            self.recipient_name = self.partner_id.name
            self.recipient_email = self.partner_id.email

    @api.onchange('recipient_email')
    def _onchange_recipient_email(self):
        """Validate email format"""
        if self.recipient_email:
            email = self.recipient_email.strip()
            # Basic email validation
            if '@' not in email or '.' not in email.split('@')[-1]:
                return {
                    'warning': {
                        'title': 'Invalid Email',
                        'message': 'Please enter a valid email address.'
                    }
                }

    def action_issue_badge(self):
        """Issue badge via IssueBadge API"""
        self.ensure_one()

        # Get API settings
        settings = self.env['issuebadge.settings'].search([
            ('company_id', '=', self.env.company.id),
            ('active', '=', True)
        ], limit=1)

        if not settings:
            raise UserError(
                'IssueBadge API is not configured.\n\n'
                'Please go to IssueBadge > Configuration > Settings and configure your API key.'
            )

        # Validate recipient email if provided
        if self.recipient_email:
            email = self.recipient_email.strip()
            if '@' not in email:
                raise UserError('Please enter a valid email address.')

        # Prepare API payload
        payload = {
            'name': self.recipient_name.strip(),
            'badge_id': self.badge_id.badge_id,
            'idempotency_key': str(uuid.uuid4())
        }

        if self.recipient_email:
            payload['email'] = self.recipient_email.strip()

        try:
            # Call IssueBadge API
            _logger.info(f'Issuing badge {self.badge_id.name} to {self.recipient_name}')

            response = requests.post(
                f'{settings.api_url}/issue/create',
                headers={
                    'Authorization': f'Bearer {settings.api_key}',
                    'Content-Type': 'application/json'
                },
                json=payload,
                timeout=30
            )

            response.raise_for_status()
            data = response.json()

            if not data.get('success'):
                error_msg = data.get('message', 'Unknown error from API')
                raise UserError(f'Failed to issue badge:\n{error_msg}')

            # Create issue record in Odoo
            issue = self.env['issuebadge.issue'].create({
                'name': data.get('IssueId', str(uuid.uuid4())),
                'badge_id': self.badge_id.id,
                'recipient_name': self.recipient_name,
                'recipient_email': self.recipient_email if self.recipient_email else False,
                'public_url': data.get('publicUrl', ''),
                'partner_id': self.partner_id.id if self.partner_id else False,
                'notes': self.notes if self.notes else False,
            })

            # Update badge statistics
            self.badge_id.write({
                'issue_count': self.badge_id.issue_count + 1,
                'last_issued_date': fields.Datetime.now()
            })

            _logger.info(f'Badge issued successfully: {issue.name}')

            # Show success notification and open the issued badge
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Badge Issued Successfully!',
                    'message': f'Certificate issued to {self.recipient_name}',
                    'type': 'success',
                    'sticky': False,
                    'next': {
                        'type': 'ir.actions.act_window',
                        'res_model': 'issuebadge.issue',
                        'res_id': issue.id,
                        'view_mode': 'form',
                        'target': 'current',
                    }
                }
            }

        except requests.exceptions.Timeout:
            raise UserError(
                'Request timed out.\n\n'
                'The IssueBadge API is taking too long to respond. Please try again.'
            )
        except requests.exceptions.ConnectionError:
            raise UserError(
                'Connection failed.\n\n'
                'Cannot connect to IssueBadge API. Please check your internet connection.'
            )
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            if status_code == 401:
                error_msg = 'Authentication failed. Please check your API key in Settings.'
            elif status_code == 404:
                error_msg = 'Badge template not found. Please sync your badges.'
            elif status_code == 429:
                error_msg = 'Rate limit exceeded. Please try again in a few minutes.'
            else:
                error_msg = f'HTTP Error {status_code}: {str(e)}'

            _logger.error(f'API Error: {error_msg}')
            raise UserError(f'Failed to issue badge:\n\n{error_msg}')

        except Exception as e:
            _logger.error(f'Unexpected error issuing badge: {str(e)}')
            raise UserError(
                f'An unexpected error occurred:\n\n{str(e)}\n\n'
                'Please check the logs for more details.'
            )

    def action_cancel(self):
        """Cancel wizard"""
        return {'type': 'ir.actions.act_window_close'}
