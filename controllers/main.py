#!/usr/bin/env python3

"""
controllers/main.py: ...

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
from models.auth import Auth
from models.main import Model
from views.main import View

from .home import HomeController
from .signin import SignInController
from .signup import SignUpController


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.signin_controller = SignInController(model, view)
        self.signup_controller = SignUpController(model, view)
        self.home_controller = HomeController(model, view)

        self.model.auth.add_event_listener("auth_changed",
                                           self.auth_state_listener)

    def auth_state_listener(self, data: Auth) -> None:
        if data.is_logged_in:
            self.home_controller.update_view()
            self.view.switch("home")
        else:
            self.view.switch("signin")

    def run(self) -> None:
        # Here, you can do operations required before launching the gui,
        # for example:
        # self.model.auth.load_auth_state()
        if self.model.auth.is_logged_in:
            self.view.switch("home")
        else:
            self.view.switch("signin")

        self.view.start_mainloop()
