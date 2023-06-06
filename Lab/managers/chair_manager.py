from decorators.decorator import limit_calls, count_arguments


class ChairManager:
    """
    This is a manager class, it contains a list of chairs and
    has methods for searching for objets
    """

    def __init__(self, chairs):
        """
        This method initializes the fields
        """
        self.chairs = chairs
        self.index = 0

    def __len__(self):
        """
        Returns the length of the list of chairs
        """
        return len(self.chairs)

    def __getitem__(self, index):
        """
        Returns the chair at the specified index
        """
        return self.chairs[index]

    def __iter__(self):
        """
        Returns an iterator object for iterating over the chairs
        """
        return self

    def __next__(self):
        """
        Returns the next item in the chairs list
        """
        if self.index >= len(self.chairs):
            self.index = 0
            raise StopIteration
        self.index += 1
        chair = self.chairs[self.index - 1]
        return chair

    def add_chair(self, chair):
        """
        method for adding objects of type chair
        :param chair:
        :return:
        """
        self.chairs.append(chair)

    def search_by_material(self, material):
        """
        method performs a search by material
        :param material:
        :return:
        """
        return filter(lambda chair: chair.material == material, self.chairs)

    def search_by_max_weight(self, max_weight):
        """
        method searches for objects greater than max_weight
        :param max_weight:
        :return:
        """
        return list(filter(lambda chair: chair.max_weight >= max_weight, self.chairs))

    def adjust_position_for_all_chairs(self, value):
        return [chair.adjust_position(value) for chair in self.chairs]

    def get_combined_with_index(self):
        """
        Returns the concatenation of each chair object with its index in the list
        """
        return enumerate(self.chairs)

    def get_combined_with_adjustment(self, value):
        """
        Returns the concatenation of each chair object with the result
         of adjust_position_for_all_chairs(value) method
        """
        return zip(self.chairs, self.adjust_position_for_all_chairs(value))

    @limit_calls(3)
    def is_chair_material_in(self, material):
        """
        Checks if all chairs have the specified material.
        """
        return all([chair.material is material for chair in self.chairs])

    @count_arguments
    def is_any_chair_owner_in(self, owner):
        """
         Checks if any chair has the specified owner.
        """
        return any([chair.owner is owner for chair in self.chairs])
