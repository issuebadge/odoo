# IssueBadge - Bulk Certificate Generator for Odoo

![IssueBadge Logo](static/description/icon.png)

Issue beautiful digital certificates and badges directly from Odoo using the IssueBadge API.

## 🌟 Features

- **Easy API Integration**: Simple Bearer token authentication
- **Badge Template Management**: Sync and manage badge templates from IssueBadge
- **Quick Badge Issuance**: Issue badges with recipient name and optional email
- **Full History Tracking**: Track all issued badges with searchable history
- **Contact Integration**: Link badges to Odoo contacts
- **Multi-Company Support**: Separate API configurations for each company
- **User Permissions**: User and Manager roles with appropriate access rights

## 📋 Requirements

- Odoo 17.0 or later (compatible with 16.0+)
- Python 3.8+
- Python `requests` library
- IssueBadge account ([Sign up here](https://app.issuebadge.com))

## 🚀 Installation

### From Odoo Apps Store

1. Search for "IssueBadge" in the Odoo Apps store
2. Click "Install"
3. Configure your API key (see Configuration section)

### Manual Installation

1. Download or clone this repository
2. Copy the `issuebadge` folder to your Odoo addons directory
3. Update the addons list: `Settings > Apps > Update Apps List`
4. Search for "IssueBadge" and click "Install"

### Install Python Dependencies

The module requires the `requests` library:

```bash
pip install requests
```

## ⚙️ Configuration

### 1. Get Your IssueBadge API Key

1. Sign up or log in at [app.issuebadge.com](https://app.issuebadge.com)
2. Go to **Settings** → **Developer Panel**
3. Click **Generate API KEY**
4. Copy the API key (you won't be able to see it again)

### 2. Configure in Odoo

1. Go to `IssueBadge > Configuration > Settings`
2. Click **Create** (or edit existing settings)
3. Enter your **IssueBadge API Key**
4. Click **Test Connection** to verify
5. Click **Save**

### 3. Sync Badge Templates

1. After saving settings, click **Sync Badges**
2. Your badge templates will be imported from IssueBadge
3. Go to `IssueBadge > Badge Templates` to view them

## 📖 Usage

### Issue a Badge (Quick Method)

1. Go to `IssueBadge > Operations > Issue Badge`
2. Select a badge template
3. Enter recipient name (required)
4. Enter recipient email (optional but recommended)
5. Optionally select an Odoo contact to link
6. Add notes if needed
7. Click **Issue Badge**

### Issue from Badge Template

1. Go to `IssueBadge > Operations > Badge Templates`
2. Click on any badge template
3. Click **Issue Badge** button
4. Fill in recipient details
5. Click **Issue Badge**

### View Issued Badges

1. Go to `IssueBadge > Operations > Issued Badges`
2. View all issued badges with filters:
   - My Issues
   - Today / This Week / This Month
   - Group by Badge Template, User, or Date
3. Click on any issued badge to view details
4. Click **View Certificate** to open the public URL

## 👥 User Permissions

### IssueBadge User
- Can issue badges
- Can view their own issued badges
- Cannot modify settings or badge templates

### IssueBadge Manager
- All User permissions
- Can configure API settings
- Can manage badge templates
- Can view all issued badges
- Can sync badges from API

Assign permissions via: `Settings > Users & Companies > Users`

## 🔐 Security & Privacy

- API keys are stored securely in Odoo database
- All API calls use HTTPS encryption
- User permissions control who can issue badges
- Company-specific configurations for multi-company setups
- No sensitive data is sent to IssueBadge except what you explicitly provide

## 🎯 Use Cases

- **Employee Training**: Issue certificates when employees complete training
- **Course Completion**: Award badges for educational achievements
- **Sales Recognition**: Reward top performers
- **Project Milestones**: Celebrate project completions
- **Compliance Certifications**: Track ISO, GDPR, etc.
- **Event Participation**: Issue attendance certificates

## 🐛 Troubleshooting

### Connection Failed

- Check your internet connection
- Verify your API key is correct
- Ensure `https://app.issuebadge.com` is accessible from your server

### Badges Not Syncing

- Verify you have created badges in your IssueBadge account
- Check API key permissions
- Click **Test Connection** first to verify authentication

### Module Not Appearing

- Update apps list: `Settings > Apps > Update Apps List`
- Check module is in correct addons path
- Check Odoo logs for errors

## 📞 Support

- **Email**: support@issuebadge.com
- **Website**: [issuebadge.com](https://issuebadge.com)
- **Documentation**: 

## 📄 License

This module is licensed under the **Odoo Proprietary License v1.0 (OPL-1)**.

See [LICENSE](LICENSE) file for details.

## 🔄 Changelog

### Version 17.0.1.0.0 (2024-10-22)

- Initial release
- API integration with IssueBadge
- Badge template management
- Badge issuance wizard
- Issued badges tracking
- Multi-company support
- User permissions (User & Manager roles)
- Contact integration

## 🤝 Contributing

This is a proprietary module. For feature requests or bug reports, please contact support@issuebadge.com

## 👨‍💻 Author

**IssueBadge Team**

- Website: [issuebadge.com](https://issuebadge.com)
- Email: support@issuebadge.com

---

Made with ❤️ by the IssueBadge Team
