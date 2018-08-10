from organisms import organism
from organisms.organism import Optional, World
from animals import animal
from random import randint


class Antelope(animal.Animal):
    def __init__(self, world: World, name: str) -> None:
        super().__init__(world, name)
        self.setType("ANTELOPE")
        self.setStrength(4)
        self.setInitiative(4)
        self.cellcolor = "red"

    def reproduce(self):
        newan: Antelope = Antelope(self.getMyWorld(),self.getName()+str(self.getMyOrderNumber())+"n")
        self.ordernumber += 1
        newan.ordernumber = self.ordernumber + 1
        newan.setXPos(self.getXPos())
        newan.setYPos(self.getYPos())
        self.getMyWorld().addToNewborns(newan)

    def action(self) -> Optional[organism.Organism]:
        enemy: organism.Organism = super().action()
        if enemy is None and self.isDead() is False:
            return super().action()
        return enemy

    def collision(self, enemy: organism.Organism) -> Optional[organism.Organism]:
        if randint(0, 1) == 1:
            if enemy.getType() != self.getType() and self.escapeFight() is True:
                return None
        return super().collision(enemy)


