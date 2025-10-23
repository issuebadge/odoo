# -*- coding: utf-8 -*-
{
    'name': 'IssueBadge Certificate Generator',
    'version': '17.0.1.0.0',
    'category': 'Productivity',
    'summary': 'Issue beautiful digital certificates and badges via IssueBadge API',
    'description': """
IssueBadge Integration for Odoo
================================

Issue professional digital certificates and badges to employees, students, customers, or partners directly from Odoo.

Key Features
------------
* **Easy API Integration**: Simple Bearer token authentication with IssueBadge
* **Badge Template Management**: Sync and manage your badge templates from IssueBadge
* **Quick Badge Issuance**: Issue badges with recipient name and optional email
* **Full History Tracking**: Track all issued badges with searchable history
* **Contact Integration**: Link badges to Odoo contacts for better organization
* **Multi-Company Support**: Separate API configurations for each company
* **Public Certificate URLs**: Each badge gets a unique shareable URL

Perfect Use Cases
-----------------
* Employee training completion certificates
* Course completion badges
* Sales achievement recognition
* Project milestone certificates
* Quality certifications (ISO, compliance)
* Event participation certificates
* Customer loyalty badges

How It Works
------------
1. Configure your IssueBadge API key in Settings
2. Sync your badge templates from IssueBadge
3. Issue badges to recipients with one click
4. Track and manage all issued certificates
5. Recipients receive beautiful, shareable digital certificates

Requirements
------------
* IssueBadge account (sign up at https://app.issuebadge.com)
* API key from IssueBadge Developer Panel

Support & Documentation
-----------------------
* Website: https://issuebadge.com
* Support: support@issuebadge.com
* Documentation: https://docs.issuebadge.com
    """,
    'author': 'IssueBadge Team',
    'website': 'https://issuebadge.com',
    'license': 'OPL-1',

    'depends': ['base', 'web'],

    'data': [
        # Security
        'security/issuebadge_security.xml',
        'security/ir.model.access.csv',

        # Views
        'views/issuebadge_settings_views.xml',
        'views/issuebadge_badge_views.xml',
        'views/issuebadge_issue_views.xml',
        'views/issuebadge_menus.xml',

        # Wizards
        'wizards/issuebadge_send_wizard_views.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'issuebadge/static/src/css/issuebadge.css',
        ],
    },

    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],

    'price': 49.00,
    'currency': 'EUR',

    'support': 'support@issuebadge.com',

    'installable': True,
    'application': True,
    'auto_install': False,
}
