#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.1
#  in conjunction with Tcl version 8.6
#    May 13, 2021 03:44:37 PM EEST  platform: Windows NT

import sys
from tkinter import END

import settings
import main

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def exit():
    print('test_support.exit')
    sys.stdout.flush()
    sys.exit()

def update():
    global w
    w.Label1['text'] = settings.virkne

def reset():
    print('test_support.reset')
    sys.stdout.flush()
    global w
    w.Text1.delete("1.0", END)
    import optionsGUI
    optionsGUI.create_Toplevel1(root)
    print(settings.virkne)

def startGame():
    if settings.virkne == 'error':
        return 0
    else:
        if len(main.gameTree) > 0:
            main.gameTree.clear()
            main.winNodes.clear()
        main.createTree(settings.virkne)
        main.printTree()
        main.createMiniMax(settings.iesak)
        main.printMiniMaxVal()
        if settings.iesak == -1:
            settings.virkne = main.AIdecide(settings.virkne)
            update()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def uzvParb():
    global w
    w.Text1.delete("1.0", END)
    if int(settings.virkne)%2 == 0:
        if settings.iesak == 1:
            w.Text1.insert(END, "Cilv. uzvarēja!")
        else:
            w.Text1.insert(END, "Dators uzvarēja!")
    else:
        if settings.iesak == 1:
            w.Text1.insert(END, "Dators uzvarēja!")
        else:
            w.Text1.insert(END, "Cilv. uzvarēja!")

def ok():
    if len(settings.virkne) == 3:
        return 0
    global w
    if w.Label1.cget("text") == "Sveiki!":
        return 0
    try:
        izv = int(w.Text1.get("1.0", 'end-1c')) - 1
        izv = izv * 2
    except:
        w.Text1.delete("1.0", END)
        w.Text1.insert(END, "error")
        return 0
    if izv > len(settings.virkne):
        w.Text1.delete("1.0", END)
        w.Text1.insert(END, "error")
        return 0
    if izv == len(settings.virkne) - 1 and len(settings.virkne) % 2 == 1:
        settings.virkne = settings.virkne[0:len(settings.virkne) - 1]
    else:
        settings.virkne = settings.virkne[0:izv] + main.saskaite(settings.virkne[izv], settings.virkne[izv + 1]) + (settings.virkne[izv + 2:len(settings.virkne)])
    update()
    print(izv)
    if len(settings.virkne) == 3:
        uzvParb()
        return 0
    settings.virkne = main.AIdecide(settings.virkne)
    update()
    if len(settings.virkne) == 3:
        uzvParb()
        return 0

if __name__ == '__main__':
    import GUI
    GUI.vp_start_gui()




