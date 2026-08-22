# CATopalian_Python_Library.pyw

import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtMultimedia import *

from src.py.theme.create_dark_palette import create_dark_palette

from src.py.scroll.create_scrollable_div import create_scrollable_div

from src.py.theme.python_highlighter import PythonHighlighter

from src.py.file.open_file import open_file

from src.py.file.show_in_file_explorer import show_in_file_explorer

####

def handle_library_click(event, file_path, text_widget, click_sound):
    """Routes the mouse click to the appropriate file action."""
    click_sound.play()
    
    if event.button() == Qt.LeftButton:
        # LEFT CLICK: Display in QTextEdit
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code_content = f.read()
            text_widget.setPlainText(code_content)
        except Exception as e:
            text_widget.setPlainText(f"Error reading file:\n{e}")
            
    elif event.button() == Qt.RightButton:
        # RIGHT CLICK: Open in VS Code
        open_file(file_path)

    elif event.button() == Qt.MiddleButton:
        # MIDDLE CLICK: Show in File Explorer
        show_in_file_explorer(file_path)

####

app = QApplication(sys.argv)
QApplication.setStyle(QStyleFactory.create('Fusion'))
app.setPalette(create_dark_palette(app))

# qss location
qssFile = os.path.join('src', 'qss', 'style001.qss')

# open, read, apply qss style sheet
with open(qssFile, "r") as style_file:
    app.setStyleSheet(style_file.read())

####

# icon location
iconFile = os.path.join('src', 'media', 'textures', 'icons', 'catopalian_true_ai.png')

####

# set app icon
app.setWindowIcon(QIcon(iconFile))

####

# sound file location
clickSoundFile = os.path.join('src', 'media', 'sounds', 'click.wav')

# setup click sound
clickSound = QSoundEffect()
clickSound.setSource(QUrl.fromLocalFile(clickSoundFile))
clickSound.setVolume(0.02)

####

# MAIN INTERFACE BUILDER (Purely Functional)

window = QWidget()
window.setWindowTitle("CATopalian Python Library")
window.resize(1200, 700)

# Main Horizontal Split Layout
main_layout = QHBoxLayout(window)
main_layout.setContentsMargins(0, 0, 0, 0)
main_layout.setSpacing(0)

# LEFT COLUMN (Sidebar)
left_menu = QWidget()
left_menu.setFixedWidth(265)
left_menu.setStyleSheet("background-color: rgb(20, 20, 20); border-right: 2px solid #555;")
left_layout = QVBoxLayout(left_menu)
left_layout.setContentsMargins(10, 10, 10, 10)
left_layout.setSpacing(10)

# Repository Title Link
title_link = QLabel("CATopalian Python Library")
title_link.setWordWrap(True)
title_link.setCursor(QCursor(Qt.PointingHandCursor))
title_link.setStyleSheet("font-size: 17px; font-weight: bold; color: rgb(170, 170, 170);")
title_link.mousePressEvent = lambda e: QDesktopServices.openUrl(
    QUrl("https://github.com/ChristopherAndrewTopalian/CATopalian_Python_Library")
)
left_layout.addWidget(title_link)

####

# Scrollable Div for Thumbnails
scroll_area, thumb_container, thumb_layout = create_scrollable_div()
left_layout.addWidget(scroll_area)
main_layout.addWidget(left_menu)

# RIGHT COLUMN (Content - defining this first so buttons can reference it)
right_content = QWidget()
right_layout = QVBoxLayout(right_content)
right_layout.setContentsMargins(20, 15, 20, 15)

# The Code Viewer 
code_viewer = QTextEdit()
code_viewer.setReadOnly(True)
code_viewer.setLineWrapMode(QTextEdit.NoWrap)

# Increased font size to 26px for massive, crisp TV viewing
code_viewer.setStyleSheet("""
    QTextEdit {
        background-color: rgb(0, 0, 0);
        border: 1px solid #555;
        border-radius: 5px;
        padding: 20px;
        font-weight: bold;
        font-family: Arial;
        font-size: 35px; 
        color: rgb(220, 220, 220); /* Standard light grey for base text */
    }
""")
right_layout.addWidget(code_viewer)

# ATTACH THE SYNTAX HIGHLIGHTER
# We pass the underlying C++ QTextDocument to the highlighter so it can paint the colors
highlighter = PythonHighlighter(code_viewer.document())

main_layout.addWidget(right_content)

####

# DYNAMIC SIDEBAR GENERATION (Recursive)
base_py_dir = os.path.join('src', 'py')

if os.path.exists(base_py_dir):
    # os.walk drills through every folder and sub-folder infinitely.
    # We sort it so the categories generate in perfect alphabetical order.
    for root, dirs, files in sorted(os.walk(base_py_dir)):
        # Gather all Python files in the current exact folder
        py_files = sorted([f for f in files if f.endswith('.py')])
        
        # If this folder actually contains Python scripts, create a UI category
        if py_files:
            # Find the relative path (e.g., 'filter\dictionary_of_dictionaries')
            rel_path = os.path.relpath(root, base_py_dir)
            
            # Format it beautifully (e.g., 'FILTER / DICTIONARY OF DICTIONARIES')
            if rel_path == '.':
                display_name = "MAIN SCRIPTS"
            else:
                display_name = rel_path.replace(os.sep, ' / ').replace('_', ' ')

            # Create the Category Header
            cat_label = QLabel(display_name.upper())
            cat_label.setStyleSheet("""
                font-size: 16px; 
                font-weight: bold; 
                color: #4dc2ff; 
                margin-top: 10px;
            """)
            thumb_layout.addWidget(cat_label)

            # Add the buttons for the scripts in this specific folder
            for file_name in py_files:
                file_path = os.path.join(root, file_name)
                
                btn = QPushButton(file_name)
                btn.setCursor(QCursor(Qt.PointingHandCursor))
                btn.setToolTip("Left: Read | Right: VS Code | Middle: Explorer")

                # We add 'b=btn' to the lambda so it knows which button to animate.
                # Then we wrap our custom function and the base C++ function in a tuple () 
                # so the lambda executes both of them back-to-back.
                btn.mousePressEvent = lambda e, p=file_path, b=btn: (
                    handle_library_click(e, p, code_viewer, clickSound),
                    QPushButton.mousePressEvent(b, e)
                )

                thumb_layout.addWidget(btn)

            # Create the Divider
            divider = QFrame()
            divider.setFrameShape(QFrame.HLine)
            divider.setFrameShadow(QFrame.Sunken)
            divider.setStyleSheet("background-color: #444; margin-bottom: 5px;")
            thumb_layout.addWidget(divider)

main_layout.addWidget(right_content)

window.show()

sys.exit(app.exec())

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

