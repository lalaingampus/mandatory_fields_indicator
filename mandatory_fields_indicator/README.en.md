# Mandatory Fields Visual Indicator (`mandatory_fields_indicator`)

<div align="center">

<img src="static/description/banner.gif" alt="Mandatory Fields Visual Indicator Banner" width="100%"/>

<br/><br/>

[![License: LGPL-3](https://img.shields.io/badge/licence-LGPL--3-blue.svg)](LICENSE)
[![Odoo Version](https://img.shields.io/badge/odoo-16.0%20%7C%2017.0%20%7C%2018.0-brightgreen.svg)](https://www.odoo.com)
[![Translation: i18n](https://img.shields.io/badge/i18n-ID%20%7C%20EN-purple.svg)](i18n/)

<br/>

[![Bahasa Indonesia](https://img.shields.io/badge/🇮🇩%20Bahasa%20Indonesia-Switch%20to%20ID-lightgrey?style=for-the-badge)](README.md)
[![English](https://img.shields.io/badge/🇬🇧%20English-Active-blue?style=for-the-badge)](README.en.md)

</div>

---

**Mandatory Fields Visual Indicator** is an Odoo module that provides modern, elegant, and fully configurable visual indicators for all required/mandatory fields across Odoo backend form views. It helps users instantly identify required inputs and prevents frustrating validation popup errors before saving.

---

## 🌟 Key Features

- 🎨 **8 Configurable Modern Visual Styles**:
  - `left_accent`: **Modern Left-Accent Bar & Asterisk** (Sleek indigo left border accent bar).
  - `soft_tint`: **Soft Dynamic Pastel Tint & Asterisk** (Gentle amber pastel background tint).
  - `badge`: **Explicit [Required] Badge Pill** (Floating crimson `[Required]` badge next to the label).
  - `gradient_glow`: **Cyber Indigo Gradient & Soft Glow** (Ultra-modern cyber glow effect with gradient highlight).
  - `pulse_dot`: **Coral Pulse Dot & Floating Tag** (Subtle pulsing coral dot micro-animation, Linear/Notion style).
  - `executive_gold`: **Executive Amber Gold Accent** (Warm luxury amber gold for enterprise systems).
  - `glassmorphism`: **Frosted Card Outline & Sapphire Glow** (Apple macOS style frosted glass outline).
  - `asterisk_only`: **Classic Red Asterisk Only** (Clean traditional red asterisk without input color modification).
- ⚡ **Zero-Reload Live Theme Switch**: Style changes in Settings take effect immediately across all backend forms without requiring a service restart or page reload.
- 🧠 **Intelligent Readonly Suppression**: Automatically removes indicators when a form or field is in `readonly` / view-only state to maintain an uncluttered presentation.
- 🚀 **Zero Database Bloat**: Lightweight implementation stored in `ir.config_parameter` and injected via session info.
- 🌐 **Multi-Language Support (i18n)**: Native bilingual support for English and Bahasa Indonesia via standard GNU gettext (`.po` / `.pot`).
- 🧩 **Broad Compatibility**: Fully compatible with standard and third-party Odoo modules (Sales, Purchase, CRM, Accounting, Inventory, HR, etc.).

---

## 📋 Requirements

### Odoo Modules:
- `web`
- `base_setup`

### Supported Odoo Versions:
- Odoo 16.0 (Community & Enterprise)
- Odoo 17.0 (Community & Enterprise)
- Odoo 18.0 (Community & Enterprise)

---

## ⚙️ Configuration

1. Navigate to **Settings** > **General Settings**.
2. Scroll to the **Mandatory Fields Visual Indicator** section.
3. Select your preferred style from the **Mandatory Field Visual Style** dropdown.
4. Click **Save**. The selected visual style is applied instantly across all backend forms.

---

## 🚀 Usage Guide

1. Open any form creation or edit view in Odoo (e.g., *Sales Order*, *Customer*, *Vendor Bill*, *Product*).
2. All mandatory/required fields will instantly display the selected visual indicators.
3. As fields are filled or switched to readonly, styles update dynamically and seamlessly.

---

## 🎨 Visual Indicator Styles Overview

| # | Style Name | Visual Appearance | Design Characteristics |
|:---|:---|:---|:---|
| **1** | **Modern Left-Accent Bar** | Indigo left accent border on inputs + Asterisk | *Clean, professional, modern UI standard* |
| **2** | **Soft Pastel Tint** | Soft pastel amber background + Asterisk | *High readability, low contrast strain on eyes* |
| **3** | **Explicit [Required] Badge** | Crimson floating `REQUIRED` badge pill | *Explicit and clear on complex and dense forms* |
| **4** | **Cyber Indigo Glow** | Indigo gradient accent with soft outer glow | *Futuristic, vibrant, and distinctive* |
| **5** | **Coral Pulse Dot** | Pulsing coral micro-dot + floating tag | *Interactive, subtle micro-interaction* |
| **6** | **Executive Amber Gold** | Warm amber gold border & light golden fill | *Executive, premium look for corporate ERPs* |
| **7** | **Sapphire Glassmorphism** | Frosted glass outline with sapphire illumination | *Clean, Apple macOS translucent design language* |
| **8** | **Classic Asterisk Only** | Traditional red asterisk `*` only | *Minimalist, standard default feel* |

---

## 👥 Contributors

* **CV. Anugerah Khair Arkananta** (<info@arkananta.id>)
* Website: [https://github.com/lalaingampus/mandatory_fields_indicator](https://github.com/lalaingampus/mandatory_fields_indicator)

---

## 📄 License

This module is licensed under **LGPL-3.0** or later.  
See the [LICENSE](LICENSE) file or [GNU Lesser General Public License](https://www.gnu.org/licenses/lgpl-3.0.html) for more details.
