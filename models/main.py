#!/usr/bin/env python3

"""
models/main.py: ...

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
from .auth import Auth


class Model:

    # Initialize the auth model. Other models can be added here.
    def __init__(self):
        self.auth = Auth()
