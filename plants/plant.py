from organisms import organism
from random import randint
from abc import ABC, abstractmethod


class Plant(organism.Organism):
    def __init__(self, world, name):
        super().__init__(world, name)
        self.setResistsPoison(True)

    def action(self):
        if self.getAge() > 10:
            rng = randint(0, 8)
            if rng == 0:
                self.spread()
        return None

    @abstractmethod
    def spread(self):
        return
