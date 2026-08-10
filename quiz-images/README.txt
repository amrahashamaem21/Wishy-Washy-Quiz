QUIZ UI ASSETS
===============

This folder contains the extracted PNG assets from the uploaded quiz UI sheet.

CONTENTS
--------
PNG files: 109

Folder structure:

characters/
    charlie/
    frieda/
buttons/
option_buttons/
feedback/
    lives/
speech_bubbles/
ui/
decorations/
misc/
washi_tape/

WHAT THE FOLDERS CONTAIN
------------------------
characters/
    Individual Charlie and Frieda character poses and expressions.

buttons/
    Main navigation buttons: Start, Next, Back, Home, Settings, Quit.

option_buttons/
    Four blank answer option button backgrounds.

feedback/
    Correct/wrong icons, stars, hearts, celebration details, and life hearts.

speech_bubbles/
    Encouragement, feedback, thought, and question bubbles.

ui/
    Quiz title, question/answer panels, score/question labels, progress bar,
    pins, binder clip, and paperclip.

decorations/
    Stars, sparkles, flowers, sun, grass, clouds, bush, fence, mailbox,
    lamp, and small doodle decorations.

misc/
    Cursors, question marks, scribbles, exclamation marks, and small doodles.

washi_tape/
    The original blue, pink, yellow, and green tape pieces, including the
    tape pieces that appear attached to specific UI cards.

TRANSPARENCY / FORMAT
---------------------
All extracted assets are PNG files saved in RGBA mode. The surrounding
background is transparent. The source artwork itself has not been
redesigned, recolored, stylized, or converted to JPG.

IMPORTANT NOTE
--------------
Some source-sheet elements intentionally appear as separate files when they
are visually separate overlays (for example, pushpins, paperclip, binder
clip, stars, tape pieces, and individual life hearts). Repeated source
instances are retained as separate files when they occur separately in the
sheet.

TKINTER / PILLOW EXAMPLE
------------------------
Install Pillow if needed:

    pip install pillow

Then load an asset:

    from PIL import Image, ImageTk
    import tkinter as tk

    root = tk.Tk()

    image = Image.open(
        "quiz_ui_assets/characters/charlie/charlie_happy.png"
    ).convert("RGBA")

    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo, bg="white")
    label.pack()

    root.mainloop()

For Tkinter buttons, the same PhotoImage object should be kept referenced
while the widget is alive, for example by storing it as an attribute.

MANIFEST
--------
ASSET_MANIFEST.txt lists every PNG file and gives a short description.
