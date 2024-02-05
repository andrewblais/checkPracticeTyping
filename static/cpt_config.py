"""
Imported by `cpt_config.py` for use in the Tkinter GUI.

Variables:
    about_text (str): Content for about popup
    help_text (str): Content for help popup
    COLOR_MAP (str - constant): Color map for determining countdown display color
    COLORS (str - constant): Color dict for retrieval of hex codes

Supplemental data/strings for use in the Tkinter GUI via cpt_main.py.
"""

# Content for about popup:
about_text = """Check/Practice Typing v.1.0\n
©2024, MIT License\n
Andrew Blais\n
https://github.com/andrewblais"""

# Content for help popup:
help_text = f"""\
A flashing cursor should appear in the blank field.\n
If you don't see the flashing cursor, click in the blank field.\n
The timer starts once you begin typing.\n
Type the text you see in bold beneath the countdown timer.\n
Hit 'Enter' to submit your entry.\n
Type the next text that appears and hit 'Enter' again.\n
Repeat.\n
Get your typing stats after 60 seconds.\n
Click 'Go again', 'Exit', or do absolutely nothing."""

# Color map for determining countdown display color:
COLOR_MAP = {5: "RED", 10: "ORANGE", 25: "YELLOW", 40: "BLUE", 60: "GREEN"}

# Color dict for retrieval of hex codes:
COLORS = {'RED': '#ec3e40',
          'ORANGE': '#ff9b2b',
          'YELLOW': '#f5d800',
          'BLUE': '#377fc7',
          'GREEN': '#01a46d',
          'BLACK': 'black',
          'DARK_GREEN': 'dark green',
          'GREY': 'grey',
          'RED4': 'red4'}
