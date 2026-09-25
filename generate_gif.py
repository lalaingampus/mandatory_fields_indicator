import os
from PIL import Image, ImageDraw, ImageFont

# Canvas Configuration
WIDTH = 1000
HEIGHT = 580
BG_COLOR = (248, 250, 252)

FONT_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
FONT_REGULAR = os.path.join(FONT_DIR, 'segoeui.ttf')
FONT_BOLD = os.path.join(FONT_DIR, 'segoeuib.ttf')
FONT_MONO = os.path.join(FONT_DIR, 'consola.ttf')

font_title = ImageFont.truetype(FONT_BOLD, 18)
font_subtitle = ImageFont.truetype(FONT_REGULAR, 12)
font_tab = ImageFont.truetype(FONT_BOLD, 12)
font_h2 = ImageFont.truetype(FONT_BOLD, 15)
font_body = ImageFont.truetype(FONT_REGULAR, 12)
font_body_bold = ImageFont.truetype(FONT_BOLD, 12)
font_small = ImageFont.truetype(FONT_REGULAR, 11)
font_small_bold = ImageFont.truetype(FONT_BOLD, 10)
font_badge = ImageFont.truetype(FONT_BOLD, 10)
font_badge_small = ImageFont.truetype(FONT_BOLD, 9)

# Define the 8 styles to cycle through in the GIF
STYLES = [
    {
        "key": "left_accent",
        "name": "Option 1: Modern Left-Accent Bar & Asterisk",
        "badge_text": "LEFT ACCENT",
        "badge_col": (79, 70, 229),
        "border_left": True,
        "bar_col": (79, 70, 229),
        "bg_col": (248, 250, 252),
        "asterisk": True,
        "show_badge": False,
        "pulse": False,
        "glow": False,
    },
    {
        "key": "soft_tint",
        "name": "Option 2: Soft Dynamic Pastel Tint & Asterisk",
        "badge_text": "PASTEL TINT",
        "badge_col": (245, 158, 11),
        "border_left": False,
        "bar_col": None,
        "bg_col": (254, 243, 199),
        "asterisk": True,
        "show_badge": False,
        "pulse": False,
        "glow": False,
    },
    {
        "key": "badge",
        "name": "Option 3: Explicit [Required] Badge Pill",
        "badge_text": "REQUIRED BADGE",
        "badge_col": (225, 29, 72),
        "border_left": False,
        "bar_col": None,
        "bg_col": (255, 255, 255),
        "asterisk": False,
        "show_badge": True,
        "pulse": False,
        "glow": False,
    },
    {
        "key": "gradient_glow",
        "name": "Option 4: Cyber Indigo Gradient & Soft Glow",
        "badge_text": "CYBER GLOW",
        "badge_col": (99, 102, 241),
        "border_left": True,
        "bar_col": (99, 102, 241),
        "bg_col": (238, 242, 255),
        "asterisk": True,
        "show_badge": False,
        "pulse": False,
        "glow": True,
    },
    {
        "key": "pulse_dot",
        "name": "Option 5: Coral Pulse Dot & Floating Tag",
        "badge_text": "PULSE DOT",
        "badge_col": (244, 63, 94),
        "border_left": False,
        "bar_col": None,
        "bg_col": (255, 241, 242),
        "asterisk": False,
        "show_badge": False,
        "pulse": True,
        "glow": False,
    },
    {
        "key": "executive_gold",
        "name": "Option 6: Executive Amber Gold Accent",
        "badge_text": "EXECUTIVE GOLD",
        "badge_col": (217, 119, 6),
        "border_left": True,
        "bar_col": (217, 119, 6),
        "bg_col": (255, 251, 235),
        "asterisk": True,
        "show_badge": False,
        "pulse": False,
        "glow": False,
    },
    {
        "key": "glassmorphism",
        "name": "Option 7: Frosted Card Outline & Sapphire Glow",
        "badge_text": "GLASSMORPHISM",
        "badge_col": (14, 165, 233),
        "border_left": False,
        "bar_col": None,
        "bg_col": (240, 249, 255),
        "asterisk": True,
        "show_badge": False,
        "pulse": False,
        "glow": True,
    },
    {
        "key": "asterisk_only",
        "name": "Option 8: Classic Red Asterisk Only",
        "badge_text": "CLASSIC ASTERISK",
        "badge_col": (239, 68, 68),
        "border_left": False,
        "bar_col": None,
        "bg_col": (255, 255, 255),
        "asterisk": True,
        "show_badge": False,
        "pulse": False,
        "glow": False,
    },
]

def draw_window_frame(draw, style_info):
    # Base background
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=(241, 245, 249))
    
    # Outer Window Card
    draw.rounded_rectangle([15, 15, WIDTH - 15, HEIGHT - 15], radius=14, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    
    # Window Title Bar
    draw.rounded_rectangle([15, 15, WIDTH - 15, 60], radius=14, fill=(248, 250, 252))
    draw.rectangle([15, 45, WIDTH - 15, 60], fill=(248, 250, 252))
    draw.line([15, 60, WIDTH - 15, 60], fill=(226, 232, 240), width=1)
    
    # Traffic lights (macOS style window buttons)
    draw.ellipse([30, 32, 42, 44], fill=(239, 68, 68))
    draw.ellipse([50, 32, 62, 44], fill=(245, 158, 11))
    draw.ellipse([70, 32, 82, 44], fill=(16, 185, 129))
    
    # Header App Info
    draw.text((100, 30), "Odoo ERP  •  Mandatory Fields Visual Indicator  •  Live Style Switcher Demo", fill=(51, 65, 85), font=font_subtitle)
    
    # Settings Bar
    draw.rounded_rectangle([30, 75, WIDTH - 30, 125], radius=8, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
    draw.text((45, 85), "Current Active Style:", fill=(100, 116, 139), font=font_small_bold)
    draw.text((45, 102), style_info["name"], fill=(15, 23, 42), font=font_body_bold)
    
    # Style Badge Pill
    badge_col = style_info["badge_col"]
    txt = style_info["badge_text"]
    tlen = draw.textlength(txt, font=font_badge)
    bx2 = WIDTH - 45
    bx1 = bx2 - tlen - 24
    draw.rounded_rectangle([bx1, 88, bx2, 112], radius=12, fill=(*badge_col[:3], 240))
    draw.text((bx1 + 12, 93), txt, fill=(255, 255, 255), font=font_badge)
    
    # Form Sheet Box
    draw.rounded_rectangle([30, 140, WIDTH - 30, HEIGHT - 30], radius=10, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    
    # Form Title
    draw.text((50, 155), "Sales Order / SO00142", fill=(15, 23, 42), font=font_title)
    draw.text((50, 180), "Draft Quotation • Customer Order Form", fill=(100, 116, 139), font=font_subtitle)
    
    draw.line([50, 205, WIDTH - 50, 205], fill=(241, 245, 249), width=1)

def draw_field(draw, x, y, w, h, label, value, is_required, style_info, placeholder=False):
    # Draw field label
    draw.text((x, y), label, fill=(71, 85, 105), font=font_body_bold)
    
    if is_required and style_info["asterisk"]:
        draw.text((x + draw.textlength(label, font=font_body_bold) + 4, y - 2), "*", fill=(239, 68, 68), font=font_h2)
        
    if is_required and style_info["show_badge"]:
        lbl_len = draw.textlength(label, font=font_body_bold)
        draw.rounded_rectangle([x + lbl_len + 8, y + 1, x + lbl_len + 68, y + 17], radius=8, fill=(254, 226, 226), outline=(239, 68, 68), width=1)
        draw.text((x + lbl_len + 14, y + 3), "REQUIRED", fill=(185, 28, 28), font=font_badge_small)
        
    if is_required and style_info["pulse"]:
        lbl_len = draw.textlength(label, font=font_body_bold)
        # Pulse dot
        draw.ellipse([x + lbl_len + 8, y + 5, x + lbl_len + 16, y + 13], fill=(244, 63, 94))
        draw.text((x + lbl_len + 22, y + 2), "Mandatory", fill=(244, 63, 94), font=font_badge_small)

    input_y = y + 22
    # Background fill
    bg = style_info["bg_col"] if is_required else (255, 255, 255)
    border_col = (203, 213, 225)
    if is_required:
        if style_info["glow"]:
            border_col = style_info["badge_col"]
            draw.rounded_rectangle([x - 2, input_y - 2, x + w + 2, input_y + h + 2], radius=8, fill=(238, 242, 255))
        elif style_info["bar_col"]:
            border_col = (148, 163, 184)
            
    draw.rounded_rectangle([x, input_y, x + w, input_y + h], radius=6, fill=bg, outline=border_col, width=1)
    
    # Left accent bar
    if is_required and style_info["border_left"] and style_info["bar_col"]:
        draw.rounded_rectangle([x, input_y, x + 4, input_y + h], radius=3, fill=style_info["bar_col"])
        
    # Text inside input
    val_color = (15, 23, 42) if not placeholder else (148, 163, 184)
    draw.text((x + (12 if (is_required and style_info["border_left"]) else 10), input_y + 8), value, fill=val_color, font=font_body)

def generate_frame(style_info):
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    draw_window_frame(draw, style_info)
    
    # Render Grid of form fields
    # Row 1
    draw_field(draw, 50, 220, 420, 36, "Customer", "Azure Interior (Brandon Freeman)", True, style_info)
    draw_field(draw, 510, 220, 420, 36, "Expiration Date", "2026-10-15", False, style_info)
    
    # Row 2
    draw_field(draw, 50, 290, 420, 36, "Invoice Address", "77 Santa Barbara Rd, Pleasant Hill CA", True, style_info)
    draw_field(draw, 510, 290, 420, 36, "Payment Terms", "Immediate Payment", True, style_info)
    
    # Row 3
    draw_field(draw, 50, 360, 420, 36, "Delivery Address", "77 Santa Barbara Rd, Pleasant Hill CA", False, style_info)
    draw_field(draw, 510, 360, 420, 36, "Pricelist", "Public Pricelist (USD)", True, style_info)
    
    # Row 4: Order Lines Table Header Preview
    draw.rounded_rectangle([50, 435, WIDTH - 50, 520], radius=8, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
    draw.text((65, 445), "Order Lines", fill=(30, 41, 59), font=font_body_bold)
    draw.line([50, 468, WIDTH - 50, 468], fill=(226, 232, 240), width=1)
    
    # Table columns
    draw.text((65, 475), "Product", fill=(100, 116, 139), font=font_small_bold)
    draw.text((450, 475), "Quantity", fill=(100, 116, 139), font=font_small_bold)
    draw.text((600, 475), "Unit Price", fill=(100, 116, 139), font=font_small_bold)
    draw.text((800, 475), "Subtotal", fill=(100, 116, 139), font=font_small_bold)
    
    draw.text((65, 495), "[DESK001] Customizable Desk (Steel Legs)", fill=(15, 23, 42), font=font_small)
    draw.text((450, 495), "5.00 Units", fill=(15, 23, 42), font=font_small)
    draw.text((600, 495), "$ 750.00", fill=(15, 23, 42), font=font_small)
    draw.text((800, 495), "$ 3,750.00", fill=(15, 23, 42), font=font_small_bold)
    
    # Status Banner
    draw.text((50, 535), "⚡ Instant Dynamic Switching • Zero Page Reload Required • Compatible with Odoo 16, 17, 18", fill=(100, 116, 139), font=font_small)
    
    return img

def create_gif(output_path):
    frames = []
    for style in STYLES:
        frame = generate_frame(style)
        # Duplicate frames for 1.5 seconds per style (duration 1500ms / 2 = ~750ms if 2 frames)
        for _ in range(3):
            frames.append(frame)
            
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=600,
        loop=0,
        optimize=True
    )
    print(f"GIF demo generated successfully at {output_path} (Size: {os.path.getsize(output_path)} bytes)")

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_gif = os.path.join(script_dir, "mandatory_fields_indicator", "static", "description", "banner.gif")
    demo_gif = os.path.join(script_dir, "mandatory_fields_indicator", "static", "description", "demo.gif")
    create_gif(target_gif)
    # Also save as demo.gif
    import shutil
    shutil.copyfile(target_gif, demo_gif)
    print(f"Copied to demo.gif: {demo_gif}")
