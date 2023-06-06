class Spider(Insect):
    def __init__(self, name, number_of_legs, has_wings, is_dangerous, can_weave_web):
        super().__init__(name, number_of_legs, has_wings, is_dangerous)
        self.can_weave_web = can_weave_web

    def can_inject_poison(self):
        return True

    def survive_over_winter(self):
        print("Spider hibernate during winter.")

    def __str__(self):
        return f"Spider(super={super().__str__()}, canWeaveWeb={self.can_weave_web})"
