# Copyright 2026 CV. Anugerah Khair Arkananta
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    "name": "Mandatory Fields Visual Indicator",
    "summary": "Configurable modern visual indicators for mandatory and required form fields across Odoo",
    "version": "16.0.1.0.0",
    "category": "Extra Tools",
    "website": "https://github.com/lalaingampus/mandatory_fields_indicator",
    "author": "CV. Anugerah Khair Arkananta",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "auto_install": False,
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
        "static/description/banner.png",
    ],
}
