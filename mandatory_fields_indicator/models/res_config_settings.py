# Copyright 2026 CV. Anugerah Khair Arkananta
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    mandatory_indicator_style = fields.Selection(
        selection=[
            ("left_accent", "Option 1: Modern Left-Accent Bar & Asterisk"),
            ("soft_tint", "Option 2: Soft Dynamic Pastel Tint & Asterisk"),
            ("badge", "Option 3: Explicit [Required] Badge Pill"),
            ("gradient_glow", "Option 4: Cyber Indigo Gradient & Soft Glow (Ultra Modern)"),
            ("pulse_dot", "Option 5: Coral Pulse Dot & Floating Tag (Linear / Notion Style)"),
            ("executive_gold", "Option 6: Executive Amber Gold Accent (Warm Luxury)"),
            ("glassmorphism", "Option 7: Frosted Card Outline & Sapphire Glow (Apple Style)"),
            ("asterisk_only", "Option 8: Classic Red Asterisk Only"),
        ],
        string="Mandatory Field Visual Style",
        default="left_accent",
        config_parameter="mandatory_fields_indicator.style",
        help="Select how mandatory/required fields are visually highlighted across the system.",
    )
