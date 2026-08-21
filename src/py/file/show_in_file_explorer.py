# show_in_file_explorer.py

import subprocess
import sys
from pathlib import Path

def show_in_file_explorer(path):
    """Reveal a file, highlighted, in the OS file manager."""
    path = str(Path(path).resolve())

    if sys.platform == 'win32':
        subprocess.Popen(f'explorer /select,"{path}"')
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', '-R', path])
    else:
        # Most Linux file managers don't support "select this file" —
        # opening the containing folder is the reliable fallback
        subprocess.Popen(['xdg-open', str(Path(path).parent)])

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

