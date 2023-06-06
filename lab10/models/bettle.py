class Beetle(Insect):
    def __init__(self, name, number_of_legs, has_wings, is_dangerous, can_roll):
        super().__init__(name, number_of_legs, has_wings, is_dangerous)
        self.can_roll = can_roll

    def can_inject_poison(self):
        return False

    def survive_over_winter(self):
        print("Beetle hibernate during winter.")

    def __str__(self):
        return f"Beetle(super={super().__str__()}, canRoll={self.can_roll})"
