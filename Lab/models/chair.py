from abc import ABC, abstractmethod


class Chair(ABC):
    """
    This is abstract chair class
    """
    special_feature = {}

    def __init__(self, id_chair=1, material="wood", max_weight="150", owner="Bob"):
        """
        This method initializes the fields
        """
        self.id_chair = id_chair
        self.material = material
        self.max_weight = max_weight
        self.owner = owner

    def __str__(self):
        """
        This method represents the object in the ribbon
        :return:
        """
        return f"Id={self.id_chair}, Material={self.material}," \
               f" Max weight={self.max_weight}, Owner={self.owner}"

    def get_attributes_by_type(self, data_type):
        """
        Returns a dictionary with attributes and their values of the specified data type
        :param data_type:
        :return:
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

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
