# -*- coding: utf-8 -*-
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
