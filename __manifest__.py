# -*- coding: utf-8 -*-
{
    "name": "Mandatory Fields Visual Indicator",
    "summary": "Configurable visual indicators (Modern Accent Bar, Soft Pastel Tint, Required Badge, Cyber Glow, Pulse Dot, Classic Asterisk) for required fields across all Odoo forms.",
    "description": """
Mandatory Fields Visual Indicator for Odoo
==========================================
Tired of frustrating validation popups when saving forms? This module provides clear, modern, and customizable visual indicators for all required/mandatory fields across Odoo backend views.

Key Features:
-------------
* 8 Distinct Visual Indicator Styles (Left-Accent Bar, Amber Tint, Required Badge, Indigo Glow, Pulse Dot, Warm Gold, Glassmorphism, Classic Asterisk).
* Instant configuration directly from Settings > General Settings without coding.
* Intelligent dynamic state handling (automatically disables indicator when fields are in readonly state).
* Ultra-lightweight SCSS styling with zero database bloat.
* Fully compatible with standard and custom modules across Odoo 16, 17, and 18.
""",
    "version": "17.0.1.0.0",
    "category": "Extra Tools",
    "author": "Open Source Community",
    "license": "LGPL-3",
    "support": "support@example.com",
    "depends": [
        "web",
        "base_setup",
    ],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "mandatory_fields_indicator/static/src/scss/mandatory_indicator.scss",
            "mandatory_fields_indicator/static/src/js/mandatory_indicator.js",
        ],
    },
    "images": [
        "static/description/icon.png",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
