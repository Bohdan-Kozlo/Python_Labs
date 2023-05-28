from models.chair import Chair


class OfficeChair(Chair):
    """
    The Office Chair class represents an office chair and inherits from the Chair class
    """

    def __init__(self, reneming=2, material="wood", max_weight="150", owner="Bob", chair_type="type",
                 material_of_upholstery="material", current_incline_back="50"):
        """
        This method initializes the fields
        :param reneming:
        :param material:
        :param max_weight:
        :param owner:
        :param chair_type:
        :param material_of_upholstery:
        :param current_incline_back:
        """
        super().__init__(reneming, material, max_weight, owner)
        self.chair_type = chair_type
        self.material_of_upholstery = material_of_upholstery
        self.current_incline_back = current_incline_back

    def adjust_position(self, value):
        """
        Method that increases the angle of inclination for an office chair
        """
        self.current_incline_back += value

    def __str__(self):
        """
        This method represents the object in the ribbon
        :return:
        """
        return super().__str__(), f"Chair type={self.chair_type},\
                Material of upholstery={self.material_of_upholstery},\
                Current incline back={self.current_incline_back}"
