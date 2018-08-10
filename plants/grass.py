from plants import plant


class Grass(plant.Plant):
    def __init__(self, world, name):
        super().__init__(world, name)
        self.setType("GRASS")
        self.cellcolor = "lightgreen"

    def spread(self):
        newpl: Grass = Grass(self.getMyWorld(), self.getName()+str(self.getMyOrderNumber())+"n")
        self.ordernumber += 1
        newpl.ordernumber = self.ordernumber + 1
        newpl.setXPos(self.getXPos())
        newpl.setYPos(self.getYPos())
        self.getMyWorld().addToNewborns(newpl)

