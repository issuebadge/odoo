# Image Creation Guide for IssueBadge Odoo Module

## Required Images

### 1. icon.png (MODULE ICON)
**Specs:**
- Size: 256x256px (or 512x512px)
- Format: PNG with transparency
- Style: Simple, recognizable at small sizes
- Colors: Purple/Blue gradient (brand colors)
- Content: Trophy, certificate, or badge icon

**Design Ideas:**
- 🏆 Trophy icon on gradient background
- 🎖️ Badge/medal icon
- 📜 Certificate scroll icon
- Combination of trophy + certificate

**Canva Template:**
1. Go to canva.com
2. Create custom size: 256 x 256 px
3. Search elements: "trophy", "certificate", "badge"
4. Background: Gradient from #667eea to #764ba2
5. Add white icon in center
6. Download as PNG (transparent background)

---

### 2. banner.png (FEATURE BANNER)
**Specs:**
- Size: 560x280px
- Format: PNG or JPG
- Style: Professional, shows value proposition
- Colors: Match icon (purple/blue)

**Content:**
```
[Left side: Icon/Graphics]    [Right side: Text]

🏆 Certificate Icon           IssueBadge
                              Certificate Generator

                              Issue Beautiful Digital
                              Certificates from Odoo
```

**Canva Steps:**
1. Custom size: 560 x 280 px
2. Add gradient background (#667eea to #764ba2)
3. Left: Add trophy/certificate graphic
4. Right: Add title "IssueBadge Certificate Generator"
5. Right: Add subtitle "Issue Beautiful Digital Certificates"
6. Download as PNG

---

### 3. Screenshots (5 IMAGES)

**Specs:**
- Size: 1024x768px (or 1920x1080px)
- Format: PNG or JPG
- Content: Actual module screenshots

**Required Screenshots:**

#### Screenshot 1: Settings Page
- File: `screenshot_1.png`
- Show: API Settings form with fields filled
- Highlight: Test Connection and Sync Badges buttons
- Caption idea: "Easy API Configuration"

#### Screenshot 2: Badge Templates
- File: `screenshot_2.png`
- Show: Badge templates in Kanban view with cards
- Highlight: Multiple badge templates displayed
- Caption idea: "Manage Your Badge Templates"

#### Screenshot 3: Issue Badge Wizard
- File: `screenshot_3.png`
- Show: Issue badge wizard form filled out
- Highlight: Recipient fields and badge selection
- Caption idea: "Issue Badges in One Click"

#### Screenshot 4: Issued Badges List
- File: `screenshot_4.png`
- Show: List view of issued badges with data
- Highlight: Search filters and issued badge records
- Caption idea: "Track All Issued Certificates"

#### Screenshot 5: Badge Detail
- File: `screenshot_5.png`
- Show: Single issued badge detail page
- Highlight: Public certificate URL
- Caption idea: "Shareable Certificate URLs"

---

## How to Take Screenshots

### Method 1: Browser Developer Tools (Best Quality)

```bash
# 1. Install module on Odoo
# 2. Open Chrome/Firefox
# 3. Press F12 (Developer Tools)
# 4. Click device icon (responsive mode)
# 5. Set resolution: 1024 x 768
# 6. Navigate to each page
# 7. Take screenshot (browser screenshot tool or Shift+Cmd+4 on Mac)
```

### Method 2: Screenshot Tool
- **Mac**: Cmd+Shift+4 (drag to select area)
- **Windows**: Win+Shift+S (snipping tool)
- **Linux**: gnome-screenshot or flameshot

### Method 3: Full Page Screenshot
- Chrome Extension: "GoFullPage"
- Firefox: Right-click → "Take Screenshot" → "Save full page"

---

## Quick Checklist

Before proceeding:
- [ ] icon.png created (256x256px)
- [ ] banner.png created (560x280px)
- [ ] screenshot_1.png (Settings)
- [ ] screenshot_2.png (Badge Templates)
- [ ] screenshot_3.png (Issue Wizard)
- [ ] screenshot_4.png (Issued List)
- [ ] screenshot_5.png (Badge Detail)
- [ ] All images saved in `static/description/` folder
- [ ] Images look good at preview size

---

## Color Scheme Reference

Use these colors for consistency:

```
Primary Purple: #667eea
Secondary Purple: #764ba2
White: #ffffff
Dark Text: #333333
Light Background: #f8f9fa
Success Green: #28a745
```

---

## Tools Recommendations

**Free:**
- Canva.com - Design tool (easiest)
- GIMP - Image editor
- Inkscape - Vector graphics
- Remove.bg - Remove backgrounds

**Paid:**
- Figma ($12/month) - Professional design
- Adobe Photoshop ($20/month)
- Sketch (Mac only, $99)

**AI Generators:**
- ideogram.ai - Free AI image generation
- midjourney.com - High quality ($10/month)
- dall-e 3 via ChatGPT Plus ($20/month)

---

## Need Help?

If you need images designed professionally:
- Fiverr.com - Search "odoo app icon" ($5-50)
- Upwork.com - Hire designer ($15-50/hour)
- 99designs.com - Design contest ($299+)

Budget option: $10-20 on Fiverr for all images
