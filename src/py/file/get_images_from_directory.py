# get_images_from_directory.py

import os

def get_images_from_directory(dir_path):
    """Reads a folder and returns all valid image filenames."""
    allowed_exts = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp"}
    files = []
    if os.path.exists(dir_path):
        try:
            for item in os.listdir(dir_path):
                ext = os.path.splitext(item)[1].lower()
                if ext in allowed_exts:
                    files.append(item)
        except Exception as err:
            print(f"Error reading directory {dir_path}: {err}")
    return files

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

