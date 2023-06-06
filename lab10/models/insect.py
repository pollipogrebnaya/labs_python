from abc import ABC, abstractmethod

class Insect(ABC):
    def __init__(self, name, number_of_legs, can_fly, has_stinger, can_inject_poison):
        self.name = name
        self.number_of_legs = number_of_legs
        self.can_fly = can_fly
        self.has_stinger = has_stinger
        self.can_inject_poison = can_inject_poison
        self.favorite_food_set = set()

    def __str__(self):
        return f"{self.name} (Legs: {self.number_of_legs}, Can Fly: {self.can_fly}, Has Stinger: {self.has_stinger}, Can Inject Poison: {self.can_inject_poison})"

    @abstractmethod
    def survive_over_winter(self):
        # Логіка виживання комахи під час зими
        if not self.can_fly and not self.has_stinger:
            raise InsectSurvivalException(self)
        return "Survived"

    def __iter__(self):
        return iter(self.favorite_food_set)
