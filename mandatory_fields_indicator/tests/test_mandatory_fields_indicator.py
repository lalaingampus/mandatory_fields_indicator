# Copyright 2026 CV. Anugerah Khair Arkananta
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from odoo.tests import common


class TestMandatoryFieldsIndicator(common.TransactionCase):
    """Unit tests for Mandatory Fields Visual Indicator module."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ConfigSettings = cls.env["res.config.settings"]
        cls.ConfigParam = cls.env["ir.config_parameter"].sudo()
        cls.IrHttp = cls.env["ir.http"]

    def test_01_default_indicator_style(self):
        """Test default indicator style retrieval from session info."""
        # Clean parameter to test default fallback
        self.ConfigParam.search([("key", "=", "mandatory_fields_indicator.style")]).unlink()

        session_info = self.IrHttp.session_info()
        self.assertIn("mandatory_indicator_style", session_info)
        self.assertEqual(session_info["mandatory_indicator_style"], "left_accent")

    def test_02_set_indicator_style(self):
        """Test updating indicator style via res.config.settings."""
        available_styles = [
            "left_accent",
            "soft_tint",
            "badge",
            "gradient_glow",
            "pulse_dot",
            "executive_gold",
            "glassmorphism",
            "asterisk_only",
        ]

        for style in available_styles:
            settings = self.ConfigSettings.create({
                "mandatory_indicator_style": style,
            })
            settings.execute()

            # Verify in ir.config_parameter
            saved_style = self.ConfigParam.get_param("mandatory_fields_indicator.style")
            self.assertEqual(saved_style, style)

            # Verify in session_info
            session_info = self.IrHttp.session_info()
            self.assertEqual(session_info["mandatory_indicator_style"], style)
