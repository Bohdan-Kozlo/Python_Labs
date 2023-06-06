class SetManager:

    def __init__(self, chair_manager):
        """Initializes the SetManager object."""
        self.chair_manager = chair_manager
        self.special_features = [special_feature for chair in self.chair_manager.chairs for special_feature in
                                 chair.special_feature]

    def __iter__(self):
        """
        Returns an iterator object for iterating over the special features.
        """
        return self

    def __next__(self):
        """
        Returns the total number of special features.
        """
        if not self.special_features:
            raise StopIteration
        return self.special_features.pop()

    def __getitem__(self, index):
        """
        Returns the special feature at the specified index.
        """
        return self.special_features[index]


