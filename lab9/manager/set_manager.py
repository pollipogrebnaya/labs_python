class SetManager:
    def __init__(self, regular_manager):
        self.regular_manager = regular_manager

    def __iter__(self):
        for insect in self.regular_manager:
            for food in insect:
                yield food

    def __len__(self):
        return sum(len(insect) for insect in self.regular_manager)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Negative indexing is not supported.")
        for insect in self.regular_manager:
            if index < len(insect):
                return list(insect)[index]
            index -= len(insect)
        raise IndexError("Index out of range.")
