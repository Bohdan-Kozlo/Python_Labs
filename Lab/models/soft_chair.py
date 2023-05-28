from models.chair import Chair


class SoftChair(Chair):
    """
    The SoftChair class represents a soft chair and is inherited from Chair
    """
    special_feature = {"Massage function"}

    def __init__(self, id_chair=2, material="wood", max_weight=150, owner="Bob", filler="filler",
                 depth="depth", cushioning=True):
        """
        This method initializes the fields
        """
        super().__init__(id_chair, material, max_weight, owner)
        self.filler = filler
        self.depth = depth
        self.cushioning = cushioning

    def __str__(self):
        """
        This method represents the object in the ribbon
        :return:
        """
        return super().__str__().rstrip(), f"Filler={self.filler},\
                Depth={self.depth},\
                Cushioning={self.cushioning}"

    def adjust_position(self, value):
        pass
