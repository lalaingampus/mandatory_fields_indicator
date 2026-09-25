# Copyright 2026 CV. Anugerah Khair Arkananta
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from odoo import models


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        result = super().session_info()
        style = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("mandatory_fields_indicator.style", default="left_accent")
        )
        result["mandatory_indicator_style"] = style
        return result
