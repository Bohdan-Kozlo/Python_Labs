class Chair:
    """
    The chair class has such fields as ID, material, maximum weight, and owner.
    Similarly, the class has methods: occupy, release, is_occupied and the static method get_instance
    """

    __instance = None

    def __init__(self, id=1, material="wood", max_weight="150", owner="Bob"):
        self.id = id
        self.material = material
        self.max_weight = max_weight
        self.owner = owner

    def __str__(self):
        return f"Id={self.id}, Material={self.material}," \
               f" Max weight={self.max_weight}, Owner={self.owner}"

    def occupy(self, owner):
        self.owner = owner

    def release(self):
        self.owner = None

    def is_occupied(self):
        return self.owner is not None

    @staticmethod
    def get_instance():
        if not Chair.__instance:
            Chair.instance = Chair()
        return Chair.__instance
