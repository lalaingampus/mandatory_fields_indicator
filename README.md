# Mandatory Fields Visual Indicator for Odoo

[![Odoo Versions](https://img.shields.io/badge/Odoo-16.0%20%7C%2017.0%20%7C%2018.0-714B67?style=flat-square&logo=odoo)](https://apps.odoo.com)
[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/lgpl-3.0)

Enhance your Odoo user experience by providing clear, customizable visual cues for mandatory / required fields across all backend form views. Prevent annoying validation popups and accelerate daily data entry.

---

## ✨ Features

- **8 Preset Visual Indicator Styles:**
  1. **Modern Left-Accent Bar** *(Default)*: Clean modern border accent with clear visual boundary.
  2. **Soft Pastel Amber Tint**: Warm soft background tint for easy scanning.
  3. **Explicit [Required] Badge**: Pill badge tag attached directly to the label.
  4. **Cyber Indigo Glow**: High-contrast purple border gradient.
  5. **Notion/Linear Pulse Dot**: Minimalist red indicator dot.
  6. **Executive Warm Gold**: Professional golden left-border with light cream background.
  7. **Glassmorphism Blue Tint**: Subtle translucent blue accent.
  8. **Classic Red Asterisk Only**: Clean asterisk next to the field label.
- **Dynamic Readonly Awareness:** Automatically removes visual cues when fields transition to readonly or form state is locked (e.g., `Confirmed`, `Done`, `Cancelled`).
- **Zero Configuration Hassle:** Change styles anytime in `Settings > General Settings` with zero coding or server restarts required.
- **Lightweight & High Performance:** Built purely with clean SCSS & lightweight Owl component lifecycle hooks.

---

## 🚀 Installation & Setup

1. Copy or clone the `mandatory_fields_indicator` directory into your Odoo `custom_addons` folder.
2. Update your Odoo Apps list:
   - Enable **Developer Mode**.
   - Go to **Apps** &rarr; **Update Apps List**.
3. Search for **Mandatory Fields Visual Indicator** and click **Install**.
4. Go to **Settings &rarr; General Settings** &rarr; scroll to **Mandatory Fields Visual Indicator** section and choose your preferred visual style.

---

## 📂 Repository Branch Structure for Odoo Apps Store

To publish to the Odoo Apps Store supporting multiple versions:

- `18.0` branch: `version: "18.0.1.0.0"`
- `17.0` branch: `version: "17.0.1.0.0"`
- `16.0` branch: `version: "16.0.1.0.0"`

---

## 📄 License
This module is licensed under the [GNU LGPL-3](https://www.gnu.org/licenses/lgpl-3.0.html).
