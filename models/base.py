#!/usr/bin/env python3

"""
models/base.py: ...

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
from typing import Callable, TypeVar, Any

Self = TypeVar("Self", bound="ObservableModel")


class ObservableModel:
    """Models that can have event listeners.

    Observable models can register callback functions for specific events.
    When any data changes, relevant events can be triggered.
    This allows all the controllers that depends on the current state of those data to
    react to the changes.
    """

    def __init__(self):

        # Create a dictionary to store the event listeners.
        self._event_listeners: dict[str, list[Callable[[Any], None]]] = {}

    def add_event_listener(self, event: str, fn: Callable[[Self], None]) -> Callable:
        """Registers event callback functions.

        Adds a callback function to the list of listeners of the specified event and
        returns a function that removes the listener from the list.

        Args:
            event (str): Name of the event.
            fn (function): Callback function to be registered.
                The function will be called with the model instance as the argument.

        Returns:
            function: Function to remove the listener function.
        """

        try:
            # If the event (key) already exists, append the function to
            # the list for corresponding key.
            self._event_listeners[event].append(fn)

        except KeyError:
            # If the event (key) does not exist, create a new list for
            # the key and add the function to the list.
            self._event_listeners[event] = [fn]

        return lambda: [self._event_listeners[event].remove(fn)]

    def trigger_event(self, event: str) -> None:

        # If the event does not exist, return.
        if event not in self._event_listeners.keys():
            return

        # Call all the functions in the list for the event.
        for func in self._event_listeners[event]:
            func(self)
