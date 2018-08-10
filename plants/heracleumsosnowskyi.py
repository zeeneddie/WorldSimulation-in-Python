from organisms import organism
from plants import plant
from organisms.organism import Optional


class Sosnowski(plant.Plant):
    def __init__(self, world, name):
        super().__init__(world, name)
        self.setType("SOSNOWSKI")
        self.setStrength(10)
        self.cellcolor = "pink"

    def action(self) -> Optional[organism.Organism]:
        startx = self.getXPos()
        starty = self.getYPos()
        check: organism.Organism = None
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= self.getXPos() + i <= self.myworld.getBoardXSize() - 1:
                    if 0 <= self.getYPos() + j <= self.myworld.getBoardYSize() - 1:
                        check: organism.Organism = self.getMyWorld().getOrganismFromBoard(startx + i, starty + j)
                    if check is not None and check.isResistantToPoison() is False and check.getName() != self.getName():
                        self.getMyWorld().killOrganism(check)

        return super().action()

    def collision(self, enemy: organism.Organism) -> Optional[organism.Organism]:
        self.getMyWorld().killOrganism(self)
        if enemy.isResistantToPoison() is False:
            self.getMyWorld().killOrganism(enemy)
        return super().collision(enemy)

    def spread(self):
        newpl: Sosnowski = Sosnowski(self.getMyWorld(), self.getName()+str(self.getMyOrderNumber())+"n")
        self.ordernumber += 1
        newpl.ordernumber = self.ordernumber + 1
        newpl.setXPos(self.getXPos())
        newpl.setYPos(self.getYPos())
        self.getMyWorld().addToNewborns(newpl)

