from models.chair import Chair


class SoftChair(Chair):
    """
    The SoftChair class represents a soft chair and is inherited from Chair
    """

    def __init__(self, reneming=2, material="wood", max_weight="150", owner="Bob", filler="filler",
                 depth="depth", cushioning=True):
        """
        This method initializes the fields
        :param reneming:
        :param material:
        :param max_weight:
        :param owner:
        :param filler:
        :param depth:
        :param cushioning:
        """
        super().__init__(reneming, material, max_weight, owner)
        self.filler = filler
        self.depth = depth
        self.cushioning = cushioning

    def __str__(self):
        """
        This method represents the object in the ribbon
        :return:
        """
        return super().__str__(), f"Filler={self.filler},\
                Depth={self.depth},\
                Cushioning={self.cushioning}"

    def adjust_position(self, value):
        pass
