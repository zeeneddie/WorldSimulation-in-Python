from organisms import organism
from organisms.organism import Optional
from animals import animal
from world import World
from random import randint


class Fox(animal.Animal):
    def __init__(self, world: World, name: str) -> None:
        super().__init__(world, name)
        self.setType("FOX")
        self.setStrength(3)
        self.setInitiative(7)
        self.cellcolor = "orange"

    def reproduce(self):
        newan: Fox = Fox(self.getMyWorld(), self.getName()+str(self.getMyOrderNumber())+"n")
        self.ordernumber += 1
        newan.ordernumber = self.ordernumber + 1
        newan.setXPos(self.getXPos())
        newan.setYPos(self.getYPos())
        self.getMyWorld().addToNewborns(newan)

    def action(self) -> Optional[organism.Organism]:
        freespotsY = []
        freespotsX = []
        iterator = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= self.getXPos() + i <= self.myworld.getBoardXSize() - 1:
                    if 0 <= self.getYPos() + j <= self.myworld.getBoardYSize() - 1:
                        enemy: organism.Organism = self.myworld.getOrganismFromBoard(self.getXPos() + i, self.getYPos() + j)
                        if (i != 0 or j != 0) and (enemy is None or enemy.getStrength() < self.getStrength()):
                            freespotsY.append(j + self.getYPos())
                            freespotsX.append(i + self.getXPos())
                            iterator += 1

        if iterator > 0:
            rng = randint(0, iterator - 1)
            self.setLastYPos(self.getYPos())
            self.setLastXPos(self.getXPos())
            self.setXPos(freespotsX[rng])
            self.setYPos(freespotsY[rng])
            enemy = self.getMyWorld().getOrganismFromBoard(self.getXPos(), self.getYPos())
            if enemy is None:
                return None
            else:
                return enemy.collision(self)
        else:
            return None
