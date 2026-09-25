/** @odoo-module **/

import { FormLabel } from "@web/views/form/form_label";
import { fieldVisualFeedback } from "@web/views/fields/field";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";

// Initialize data-mandatory-style on DOM root so SCSS responds to config
const activeStyle = session.mandatory_indicator_style || "left_accent";
if (typeof document !== "undefined") {
    const applyStyle = () => {
        document.documentElement.setAttribute("data-mandatory-style", activeStyle);
        if (document.body) {
            document.body.setAttribute("data-mandatory-style", activeStyle);
        }
    };
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", applyStyle);
    } else {
        applyStyle();
    }
}

/**
 * Patch FormLabel component so that every required field's label
 * receives the 'o_required_modifier' CSS class automatically.
 */
patch(FormLabel.prototype, {
    get className() {
        const res = super.className || "";
        if (!this.props || !this.props.fieldInfo || !this.props.record) {
            return res;
        }
        try {
            const { readonly, required } = fieldVisualFeedback(
                this.props.fieldInfo.field,
                this.props.record,
                this.props.fieldName,
                this.props.fieldInfo
            );
            if (required && !readonly && !res.includes("o_required_modifier")) {
                return (res + " o_required_modifier").trim();
            }
        } catch (e) {
            // gracefully ignore evaluation errors
        }
        return res;
    },
});
