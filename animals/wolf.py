from animals import animal
from world import World


class Wolf(animal.Animal):
    def __init__(self, world: World, name: str) -> None:
        super().__init__(world, name)
        self.setType("WOLF")
        self.setStrength(9)
        self.setInitiative(5)
        self.cellcolor = "gray"

    def reproduce(self):
        newan: Wolf = Wolf(self.getMyWorld(), self.getName()+str(self.getMyOrderNumber())+"n")
        self.ordernumber += 1
        newan.ordernumber = self.ordernumber + 1
        newan.setXPos(self.getXPos())
        newan.setYPos(self.getYPos())
        self.getMyWorld().addToNewborns(newan)