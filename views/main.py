#!/usr/bin/env python3

"""
views/main.py: ...

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
from typing import TypedDict

from .master import Master
from .home import HomeView
from .signin import SignInView
from .signup import SignUpView


class Frames(TypedDict):
    signup: SignUpView
    signin: SignInView
    home: HomeView


class View:
    def __init__(self):

        # Create the master window and empty dictionary for frames.
        self.master = Master()
        self.frames: Frames = {}  # type: ignore

        # Add all frames to the master.
        self._add_frame(SignUpView, "signup")
        self._add_frame(SignInView, "signin")
        self._add_frame(HomeView, "home")

    def _add_frame(self, frame, name: str) -> None:
        self.frames[name] = frame(self.master)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.master.mainloop()


# To destroy each frame after switching to another frame, we need to
# modify the code and also view/controller.
# class View:
#     def __init__(self):
#         self.root = Root()
#         self.frame_classes = {
#             "signin": SignInView,
#             "signup": SignUpView,
#             "home": HomeView,
#         }
#         self.current_frame = None
#
#     def switch(self, name):
#         new_frame = self.frame_classes[name](self.root)
#         if self.current_frame is not None:
#             self.current_frame.destroy()
#         self.current_frame = new_frame
#         self.current_frame.grid(row=0, column=0, sticky="nsew")
#
#     def start_mainloop(self):
#         self.root.mainloop()
