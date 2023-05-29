class Insect:
    def __init__(self, name="Insect", number_of_legs=0, has_wings=False, is_dangerous=False, is_sleeping=False):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous
        self.is_sleeping = is_sleeping

    def is_poisonous(self):
        return self.is_dangerous

    def hibernate(self):
        self.is_sleeping = True
        print(self.name + " is hibernating...\n")

    def wake_up(self):
        self.is_sleeping = False
        print("\n" + self.name + " is waking up...")

    def __str__(self):
        return f"Insect(name={self.name}, numberOfLegs={self.number_of_legs}, hasWings={self.has_wings}, " \
               f"isDangerous={self.is_dangerous}, isSleeping={self.is_sleeping})"

    @staticmethod
    def get_instance():
        if not hasattr(Insect, "instance"):
            Insect.instance = Insect()
        return Insect.instance
