# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IssueBadgeIssue(models.Model):
    _name = 'issuebadge.issue'
    _description = 'Issued Badges'
    _order = 'create_date desc'
    _rec_name = 'recipient_name'

    name = fields.Char(
        string='Issue ID',
        required=True,
        readonly=True,
        help='Unique identifier from IssueBadge API'
    )
    badge_id = fields.Many2one(
        'issuebadge.badge',
        string='Badge Template',
        required=True,
        ondelete='restrict',
        help='Badge template that was issued'
    )
    badge_name = fields.Char(
        related='badge_id.name',
        string='Badge Name',
        store=True,
        readonly=True
    )
    recipient_name = fields.Char(
        string='Recipient Name',
        required=True,
        help='Name of the badge recipient'
    )
    recipient_email = fields.Char(
        string='Recipient Email',
        help='Email address of the recipient (optional)'
    )
    public_url = fields.Char(
        string='Certificate URL',
        readonly=True,
        help='Public URL where the certificate can be viewed'
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Related Contact',
        help='Link to Odoo contact if available'
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True
    )
    create_date = fields.Datetime(
        string='Issued On',
        readonly=True
    )
    user_id = fields.Many2one(
        'res.users',
        string='Issued By',
        default=lambda self: self.env.user,
        readonly=True
    )
    notes = fields.Text(
        string='Notes',
        help='Additional notes about this badge issuance'
    )

    _sql_constraints = [
        ('name_unique', 'unique(name)',
         'This Issue ID already exists!')
    ]

    def action_open_certificate(self):
        """Open certificate URL in browser"""
        self.ensure_one()

        if not self.public_url:
            from odoo.exceptions import UserError
            raise UserError('No certificate URL available for this badge.')

        return {
            'type': 'ir.actions.act_url',
            'url': self.public_url,
            'target': 'new',
        }

    def action_view_partner(self):
        """View related partner/contact"""
        self.ensure_one()

        if not self.partner_id:
            from odoo.exceptions import UserError
            raise UserError('No contact linked to this badge.')

        return {
            'name': 'Contact',
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'res_id': self.partner_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
