from plants import plant


class Dandelion(plant.Plant):
    def __init__(self, world, name):
        super().__init__(world, name)
        self.setType("DANDELION")
        self.cellcolor = "yellow"


    def action(self):
        for i in range(0, 3):
            super().action()
        return None

    def spread(self):
        newpl: Dandelion = Dandelion(self.getMyWorld(), self.getName()+str(self.getMyOrderNumber())+"n")
        self.ordernumber += 1
        newpl.ordernumber = self.ordernumber + 1
        newpl.setXPos(self.getXPos())
        newpl.setYPos(self.getYPos())
        self.getMyWorld().addToNewborns(newpl)