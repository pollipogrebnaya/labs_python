from abc import ABC, abstractmethod

class Insect(ABC):
    def __init__(self, name, number_of_legs, has_wings=False, is_dangerous=False):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous

    @abstractmethod
    def can_inject_poison(self):
        pass

    @abstractmethod
    def survive_over_winter(self):
        pass

    def __str__(self):
        return f"Insect: name={self.name}, number_of_legs={self.number_of_legs}, has_wings={self.has_wings}, is_dangerous={self.is_dangerous}"
