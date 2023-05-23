#!/usr/bin/env python3

"""
models/auth.py: ...

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
from typing import TypedDict, Union
from .base import ObservableModel


class User(TypedDict):
    username: str


class Auth(ObservableModel):
    def __init__(self):
        super().__init__()
        self.is_logged_in = False
        self.current_user: Union[User, None] = None

    def login(self, user: User) -> None:
        self.is_logged_in = True
        self.current_user = user
        self.trigger_event("auth_changed")

    def logout(self) -> None:
        self.is_logged_in = False
        self.current_user = None
        self.trigger_event("auth_changed")
