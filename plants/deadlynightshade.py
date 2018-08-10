from organisms import organism
from plants import plant


class DeadlyNightshade(plant.Plant):
    def __init__(self, world, name):
        super().__init__(world, name)
        self.setType("DEADLYNIGHTSHADE")
        self.setStrength(99)
        self.cellcolor = "purple"

    def spread(self):
        newpl: DeadlyNightshade = DeadlyNightshade(self.getMyWorld(), self.getName()+str(self.getMyOrderNumber())+"n")
        self.ordernumber += 1
        newpl.ordernumber = self.ordernumber + 1
        newpl.setXPos(self.getXPos())
        newpl.setYPos(self.getYPos())
        self.getMyWorld().addToNewborns(newpl)

    def collision(self, enemy: organism.Organism):
        self.getMyWorld().killOrganism(self)
        if enemy.isResistantToPoison() is not True:
            self.getMyWorld().killOrganism(enemy)
        return None
