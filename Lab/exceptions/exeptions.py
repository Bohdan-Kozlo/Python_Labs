class InvalidChairPositionError(Exception):
    def __init__(self, position):
        self.position = position
        self.massage = f"Invalid chair position: {position}"
        super().__init__(self.massage)
