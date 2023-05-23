#!/usr/bin/env python3

"""
main.py: ...

This module is responsible for ...
Inspired by
https://nazmul-ahsan.medium.com/how-to-organize-multi-
frame-tkinter-application-with-mvc-pattern-79247efbb02b and
https://github.com/AhsanShihab/tkinter-multiframe-mvc/tree/master
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
from views.main import View
from controllers.main import Controller


def main():
    """
    The main function is the entry point of the program.
    It creates an instance of Model, View and Controller.
    Then it starts the controller.

    :return: None
    """

    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.run()


# Execute main function.
if __name__ == "__main__":
    main()
