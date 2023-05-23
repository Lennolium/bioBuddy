#!/usr/bin/env python3

"""
views/master.py: ...

This module is responsible for ...
"""

# Header.
__author__ = "Lennart Haack"
__email__ = "lennart-haack@stud.uni-frankfurt.de"
__license__ = "GNU GPLv3"
__version__ = "TODO: X.Y.Z"
__date__ = "2023-05-23"
__status__ = "TODO: Prototype/Development/Production"

# Imports.
import tkinter as tk


# Inheriting methods and attributes from tk.Tk.
class Master(tk.Tk):
    def __init__(self):
        super().__init__()

        start_width = 500
        min_width = 400
        start_height = 300
        min_height = 250

        self.update()
        x_offset = (self.winfo_screenwidth() - start_width) // 2
        y_offset = (self.winfo_screenheight() - start_height) // 2
        self.geometry(f"{start_width}x{start_height}+{x_offset}+{y_offset}")

        self.minsize(width=min_width, height=min_height)
        self.title("🐕 GeneHound")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
