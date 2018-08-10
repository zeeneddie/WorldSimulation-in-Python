from organisms import organism
from organisms.organism import Optional, World
from animals import animal
from random import randint


class Turtle(animal.Animal):
    def __init__(self, world: World, name: str) -> None:
        super().__init__(world, name)
        self.setType("TURTLE")
        self.setStrength(2)
        self.setInitiative(1)
        self.cellcolor = "green"

    def reproduce(self):
        newan: Turtle = Turtle(self.getMyWorld(), self.getName()+str(self.getMyOrderNumber())+"n")
        self.ordernumber += 1
        newan.ordernumber = self.ordernumber + 1
        newan.setXPos(self.getXPos())
        newan.setYPos(self.getYPos())
        self.getMyWorld().addToNewborns(newan)

    def action(self):
        rng = randint(0, 3)
        if rng == 3:
            return super().action()
        else:
            return None

    def collision(self, enemy: organism.Organism) -> Optional[organism.Organism]:
        if enemy.getType() != self.getType() and Turtle.didIReflect(enemy) is True:
            enemy.cancelMove()
            return None
        else:
            return super().collision(enemy)

    @staticmethod
    def didIReflect(enemy: organism.Organism):
        return enemy.getStrength() < 5
