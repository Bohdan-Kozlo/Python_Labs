from abc import ABC, abstractmethod


class Chair(ABC):
    """
    This is abstract chair class
    """

    def __init__(self, reneming=1, material="wood", max_weight="150", owner="Bob"):
        """
        This method initializes the fields
        :param reneming:
        :param material:
        :param max_weight:
        :param owner:
        """
        self.reneming = reneming
        self.material = material
        self.max_weight = max_weight
        self.owner = owner

    def __str__(self):
        """
        This method represents the object in the ribbon
        :return:
        """
        return f"Id={self.reneming}, Material={self.material}," \
               f" Max weight={self.max_weight}, Owner={self.owner}"

    def occupy(self, owner):
        """
        Method that specifies that the chair is currently occupied by the owner
        :param owner:
        :return:
        """
        self.owner = owner

    def release(self):
        """
        Method that frees the chair
        """
        self.owner = None

    def is_occupied(self):
        """
        Method that returns true if the seat is free
        """
        return self.owner is not None

    @abstractmethod
    def adjust_position(self, value):
        """
        An empty method that is overridden in the class FeedingTable and OfficeChair
        """
