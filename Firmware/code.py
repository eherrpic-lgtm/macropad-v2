import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

OPEN_TERMINAL = KC.MACRO(
    KC.LCMD(KC.SPACE), 
    KC.MACRO_SLEEP_MS(120),
    "iTerm2",
    KC.MACRO_SLEEP_MS(120),
    KC.ENTER
)

OPEN_SURFSHARK = KC.MACRO(
    KC.LCMD(KC.SPACE), 
    KC.MACRO_SLEEP_MS(120),
    "Surfshark",
    KC.MACRO_SLEEP_MS(120),
    KC.ENTER
)

OPEN_FINDER = KC.MACRO(
    KC.LCMD(KC.SPACE), 
    KC.MACRO_SLEEP_MS(120),
    "Finder",
    KC.MACRO_SLEEP_MS(120),
    KC.ENTER
)

# 1. Enable Layers & Encoder Modules
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

# 2. Key Matrix Configuration (3 Rows x 4 Columns = 12 Switches)
# Adjust these pins if your schematic uses a different pin ordering
keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D3, board.D4, board.D5, board.D6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 3. Rotary Encoders (Pin A, Pin B) - Rotational inputs only
encoder_handler.pins = (
    (board.D7, board.D8, None),   # Encoder 1 (e.g., Volume control)
    (board.D9, board.D10, None),  # Encoder 2 (e.g., Scroll / Zoom)
)

# 4. Rotary Encoder Actions: [ [(CCW, CW), (CCW, CW)], ... ]
encoder_handler.map = [
    # Layer 0 (macOS)
    [
        (KC.VOLD, KC.VOLU),          # Encoder 1: Volume Down / Volume Up
        (KC.BRID, KC.BRIU),  # Encoder 2: Scroll Up / Scroll Down
    ],
    # Layer 1 (Windows)
    [
        (KC.VOLD, KC.VOLU),          # Encoder 1: Volume Down / Volume Up
        (KC.BRID, KC.BRIU),  # Encoder 2: Scroll Up / Scroll Down
    ],
]

# 5. Keymap Layouts (12 Keys)
keyboard.keymap = [
    # --- Layer 0: macOS (Uses Cmd / KC.LCMD) ---
    [
        KC.MPLY(KC.C), KC.LCMD(KC.V), KC.LCMD(KC.Z), KC.LCMD(KC.X),
        KC.MPLY,         KC.MPRV,         KC.MNXT,         KC.MUTE,
        OPEN_TERMINAL,        OPEN_SURFSHARK,        OPEN_FINDER,        KC.TO(1),   # Key 12: Switch to Windows Mode
    ],
    # --- Layer 1: Windows (Uses Ctrl / KC.LCTL) ---
    [
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Z), KC.LCTL(KC.X),
        KC.MPLY,         KC.MPRV,         KC.MNXT,         KC.MUTE,
        KC.MUTE,        KC.MPLY,        KC.MNXT,        KC.TO(0),   # Key 12: Switch to macOS Mode
    ],
]

if __name__ == '__main__':
    keyboard.go()