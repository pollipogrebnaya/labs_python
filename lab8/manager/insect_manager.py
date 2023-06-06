class InsectManager:
    def __init__(self):
        self.insects = []

    def add_insect(self, insect):
        self.insects.append(insect)

    def find_insects_by_number_of_legs(self, number_of_legs):
        return [insect for insect in self.insects if insect.get_number_of_legs() == number_of_legs]

    def find_insects_that_can_inject_poison(self):
        return [insect for insect in self.insects if insect.can_inject_poison()]
