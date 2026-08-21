# open_file.py

import os
import sys
import subprocess

def open_file(whichFilePath):
    if os.path.exists(whichFilePath):
        if sys.platform == 'win32':
            os.startfile(whichFilePath)
        elif sys.platform == 'darwin':
            subprocess.call(('open', whichFilePath))
        else:
            subprocess.call(('xdg-open', whichFilePath))
    else:
        print('File not found:', whichFilePath)

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

