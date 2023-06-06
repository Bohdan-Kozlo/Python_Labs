"""
This file contains custom exception
"""


class InvalidChairPositionError(Exception):
    """
    This is an exception that is responsible for generating
    an error when the position of the chair is incorrectly set
    """
    def __init__(self, position):
        self.position = position
        self.massage = f"Invalid chair position: {position}"
        super().__init__(self.massage)
