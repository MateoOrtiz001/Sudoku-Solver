from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

def set_label_font(label, font_family="Arial", font_size=16, bold=False, italic=False):
    font = QFont(font_family, font_size)
    font.setBold(bold)
    font.setItalic(italic)
    label.setFont(font)

def set_label_color(label, color="#000000", background=None):
    palette = label.palette()
    palette.setColor(QPalette.WindowText, QColor(color))
    if background:
        palette.setColor(QPalette.Window, QColor(background))
        label.setAutoFillBackground(True)
    label.setPalette(palette)

def set_label_alignment(label, alignment="center"):
    alignments = {
        "left": Qt.AlignLeft,
        "right": Qt.AlignRight,
        "center": Qt.AlignCenter,
        "justify": Qt.AlignJustify
    }
    label.setAlignment(alignments.get(alignment, Qt.AlignCenter))

def set_label_margin(label, margin=10):
    label.setMargin(margin)
    
def set_button_style(button, background="#1E1E1E", color="#FFFFFF", font_size=14, padding=10, border_radius=2):
    style = f"""
    QPushButton {{
        background-color: {background};
        color: {color};
        font-size: {font_size}px;
        padding: {padding}px;
        border-radius: {border_radius}px;
    }}
    QPushButton:hover {{
        background-color: #191919;
    }}
    QPushButton:pressed {{
        background-color: #2E2E2E;
    }}
    """
    button.setStyleSheet(style)