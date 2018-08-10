from organisms import organism
from plants import plant
from organisms.organism import Optional


class Guarana(plant.Plant):
    def __init__(self, world, name):
        super().__init__(world, name)
        self.setType("GUARANA")
        self.cellcolor = "Chocolate"

    def collision(self, enemy) -> Optional[organism.Organism]:
        Guarana.applyStrengthBuff(enemy)
        return super().collision(enemy)

    @staticmethod
    def applyStrengthBuff(enemy: organism.Organism):
        enemy.setStrength(enemy.getStrength() + 3)

    def spread(self):
        newpl: Guarana = Guarana(self.getMyWorld(), self.getName()+str(self.getMyOrderNumber())+"n")
        self.ordernumber += 1
        newpl.ordernumber = self.ordernumber + 1
        newpl.setXPos(self.getXPos())
        newpl.setYPos(self.getYPos())
        self.getMyWorld().addToNewborns(newpl)

