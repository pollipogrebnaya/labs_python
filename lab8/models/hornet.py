class Hornet(Insect):
    def __init__(self, name, number_of_legs, has_wings, is_dangerous, can_bite):
        super().__init__(name, number_of_legs, has_wings, is_dangerous)
        self.can_bite = can_bite

    def can_inject_poison(self):
        return self.can_bite

    def survive_over_winter(self):
        print("Hornet hibernate during winter...")

    def __str__(self):
        return f"Hornet(super={super().__str__()}, canBite={self.can_bite})"
