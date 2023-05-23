#!/usr/bin/env python3

"""
views/signin.py: ...

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


class SignInView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.header = tk.Label(self, text="Sign In with existing account")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.username_label = tk.Label(self, text="Username")
        self.username_input = tk.Entry(self)
        self.username_label.grid(row=1, column=0, padx=10, sticky="w")
        self.username_input.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        self.password_label = tk.Label(self, text="Password")
        self.password_input = tk.Entry(self, show="*")
        self.password_label.grid(row=2, column=0, padx=10, sticky="w")
        self.password_input.grid(row=2, column=1, padx=(0, 20), sticky="ew")

        self.signin_btn = tk.Button(self, text="Sign In")
        self.signin_btn.grid(row=3, column=1, padx=0, pady=10, sticky="w")

        self.signup_option_label = tk.Label(self, text="Don't have an "
                                                       "account?")
        self.signup_btn = tk.Button(self, text="Sign Up")
        self.signup_option_label.grid(row=4, column=1, sticky="w")
        self.signup_btn.grid(row=5, column=1, sticky="w")
