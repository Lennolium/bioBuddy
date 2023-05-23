#!/usr/bin/env python3

"""
controllers/signin.py: ...

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
from models.main import Model
from models.auth import User
from views.main import View


class SignInController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["signin"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signin_btn.config(command=self.signin)
        self.frame.signup_btn.config(command=self.signup)

    def signup(self) -> None:
        self.view.switch("signup")

    def signin(self) -> None:
        username = self.frame.username_input.get()
        pasword = self.frame.password_input.get()
        data = {"username": username, "password": pasword}
        print(data)
        self.frame.password_input.delete(0, last=len(pasword))
        user: User = {"username": data["username"]}
        self.model.auth.login(user)