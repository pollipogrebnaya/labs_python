class Insect:
    def __init__(self, name, number_of_legs, can_fly, has_stinger, can_inject_poison):
        self.name = name
        self.number_of_legs = number_of_legs
        self.can_fly = can_fly
        self.has_stinger = has_stinger
        self.can_inject_poison = can_inject_poison

    def __str__(self):
        return f"{self.name} (Legs: {self.number_of_legs}, Can Fly: {self.can_fly}, Has Stinger: {self.has_stinger}, Can Inject Poison: {self.can_inject_poison})"


class InsectManager:
    def __init__(self):
        self.insects = []

    def add_insect(self, insect):
        self.insects.append(insect)

    def find_insects_by_number_of_legs(self, number_of_legs):
        return [insect for insect in self.insects if insect.number_of_legs == number_of_legs]

    def find_insects_that_can_inject_poison(self):
        return [insect for insect in self.insects if insect.can_inject_poison]


manager = InsectManager()

manager.add_insect(Insect("Anopheles", 6, True, True, True))
manager.add_insect(Insect("Aedes albopictus", 6, True, True, True))
manager.add_insect(Insect("Vespa bicolor", 6, True, True, True))
manager.add_insect(Insect("Vespa crabro", 6, True, True, True))
manager.add_insect(Insect("Scarabaeus sacer", 6, False, False, True))
manager.add_insect(Insect("Curculionidae", 6, False, False, True))
manager.add_insect(Insect("Black widow", 8, False, True, True))
manager.add_insect(Insect("Sparassidae", 8, False, True, True))

print("Insects with 6 legs:")
for insect in manager.find_insects_by_number_of_legs(6):
    print(insect)

print("\nInsects that can inject poison:")
for insect in manager.find_insects_that_can_inject_poison():
    print(insect)
