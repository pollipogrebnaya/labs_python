class Insect:
    def __init__(self, name, number_of_legs, can_fly, has_stinger, can_inject_poison):
        self.name = name
        self.number_of_legs = number_of_legs
        self.can_fly = can_fly
        self.has_stinger = has_stinger
        self.can_inject_poison = can_inject_poison

    def __str__(self):
        return f"{self.name} (Legs: {self.number_of_legs}, Can Fly: {self.can_fly}, Has Stinger: {self.has_stinger}, Can Inject Poison: {self.can_inject_poison})"

    def survive_over_winter(self):
        # Логіка виживання комахи під час зими
        return "Survived"


class InsectManager:
    def __init__(self):
        self.insects = []

    def add_insect(self, insect):
        self.insects.append(insect)

    def find_insects_by_number_of_legs(self, number_of_legs):
        return [insect for insect in self.insects if insect.number_of_legs == number_of_legs]

    def find_insects_that_can_inject_poison(self):
        return [insect for insect in self.insects if insect.can_inject_poison]

    def __len__(self):
        return len(self.insects)

    def __getitem__(self, index):
        return self.insects[index]

    def __iter__(self):
        return iter(self.insects)

    def get_results_of_survive_over_winter(self):
        return [insect.survive_over_winter() for insect in self.insects]

    def get_numbered_objects(self):
        return list(enumerate(self.insects))

    def get_pairs_with_survival_results(self):
        return list(zip(self.insects, self.get_results_of_survive_over_winter()))

    def get_attributes_by_type(self, attribute_type):
        return {key: value for key, value in self.insects[0].__dict__.items() if isinstance(value, attribute_type)}

    def check_conditions(self, condition):
        return {"all": all(condition(insect) for insect in self.insects),
                "any": any(condition(insect) for insect in self.insects)}


# Приклад використання класу InsectManager з усіма методами
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

print("\nNumber of insects:", len(manager))

print("\nFirst insect:", manager[0])

print("\nAll insects:")
for insect in manager:
    print(insect)

print("\nSurvival results over winter:")
results = manager.get_results_of_survive_over_winter()
for insect, result in zip(manager, results):
    print(f"{insect}: {result}")

print("\nAttributes by type (bool):")
bool_attributes = manager.get_attributes_by_type(bool)
for attribute, value in bool_attributes.items():
    print(f"{attribute}: {value}")

print("\nChecking conditions (Has stinger):")
conditions = manager.check_conditions(lambda insect: insect.has_stinger)
print("All insects have a stinger:", conditions["all"])
print("At least one insect has a stinger:", conditions["any"])
