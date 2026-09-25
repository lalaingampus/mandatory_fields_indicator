# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [18.0.1.0.0] - 2026-09-25

### Added
- **8 Configurable Visual Indicator Styles**:
  - `left_accent`: Modern Left-Accent Bar & Asterisk (Default, clean left border with accent).
  - `soft_tint`: Soft Dynamic Pastel Tint & Asterisk (Subtle background fill).
  - `badge`: Explicit `[Required]` Badge Pill (Unambiguous floating badge).
  - `gradient_glow`: Cyber Indigo Gradient & Soft Glow (Ultra modern UI with smooth shadow).
  - `pulse_dot`: Coral Pulse Dot & Floating Tag (Linear / Notion style micro-animation).
  - `executive_gold`: Executive Amber Gold Accent (Warm luxury enterprise look).
  - `glassmorphism`: Frosted Card Outline & Sapphire Glow (Apple macOS glass design).
  - `asterisk_only`: Classic Red Asterisk Only (Minimalist standard indicator).
- **Zero-Reload Dynamic Theme Injection**:
  - Live session parameter synchronization via `ir.http.session_info`.
  - Client-side OWL `mandatory_indicator.js` dynamic stylesheet observer and injection.
- **Intelligent Field State Recognition**:
  - Automatically suppresses indicator styling when fields switch to `readonly` or view-only mode.
  - Full support for `o_field_widget`, `o_input`, `o_datepicker_input`, textareas, many2one, and custom selection dropdowns.
- **Settings Integration**:
  - Native configuration under **Settings > General Settings > Mandatory Fields Visual Indicator**.
  - No database migration or schema modification needed; purely config-driven.
- **Documentation & Localization**:
  - OCA-standard `readme/` documentation fragments (`DESCRIPTION.md`, `CONFIGURATION.md`, `USAGE.md`, `CONTRIBUTORS.md`).
  - Native gettext translations in English (`pot`) and Bahasa Indonesia (`id.po`, `id_ID.po`).
  - Unit test suite covering configuration defaults, parameter updates, and session info enrichment.
