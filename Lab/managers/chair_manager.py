
class ChairManager:
    """
    This is a manager class, it contains a list of chairs and
    has methods for searching for objets
    """

    def __init__(self, chairs):
        """
        This method initializes the fields
        :param chairs:
        """
        self.chairs = chairs

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
    