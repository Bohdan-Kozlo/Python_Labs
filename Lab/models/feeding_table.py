from models.chair import Chair


class FeedingTable(Chair):
    """
    The FeedingTable class represents a chair for feeding a baby,
     which inherits from the Chair class.
    """

    def __init__(self, reneming=2, material="wood", max_weight="150", owner="Bob", max_height_chair=100, min_height_chair=60,
                 age_child=2, current_height_chair=70):
        """
        This method initializes the fields
        :param reneming:
        :param material:
        :param max_weight:
        :param owner:
        :param max_height_chair:
        :param min_height_chair:
        :param age_child:
        :param current_height_chair:
        """
        super().__init__(reneming, material, max_weight, owner)
        self.max_height_chair = max_height_chair
        self.min_height_chair = min_height_chair
        self.age_child = age_child
        self.current_height_chair = current_height_chair

    def adjust_position(self, value):
        """
        Method that will increase the height of the feeding chair
        """
        self.current_height_chair += value

    def __str__(self):
        """
        This method represents the object in the ribbon
        :return:
        """
        return super().__str__(), f"Max Height chair={self.max_height_chair},\
                Min height chair={self.min_height_chair}, \
                Age Child={self.age_child}, \
                Current height chair={self.current_height_chair}"
