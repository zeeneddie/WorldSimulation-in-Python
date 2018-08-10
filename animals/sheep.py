from animals import animal
from world import World


class Sheep(animal.Animal):
    def __init__(self, world: World, name: str) -> None:
        super().__init__(world, name)
        self.setType("SHEEP")
        self.setStrength(4)
        self.setInitiative(4)
        self.cellcolor = "black"

    def reproduce(self):
        newan: Sheep = Sheep(self.getMyWorld(), self.getName()+str(self.getMyOrderNumber())+"n")
        self.ordernumber += 1
        newan.ordernumber = self.ordernumber + 1
        newan.setXPos(self.getXPos())
        newan.setYPos(self.getYPos())
        self.getMyWorld().addToNewborns(newan)
