from world import World
from animals import sheep
from organisms.organism import Organism
from random import randint


class CyberSheep(sheep.Sheep):
    def __init__(self, world: World, name: str) -> None:
        super().__init__(world, name)
        self.setType("CYBERSHEEP")
        self.setStrength(11)
        self.setInitiative(4)
        self.cellcolor = "magenta"
        self.setResistsPoison(True)
        self.huntTarget: Organism = None

    def reproduce(self):
        newan: CyberSheep = CyberSheep(self.getMyWorld(), self.getName()+str(self.getMyOrderNumber())+"n")
        self.ordernumber += 1
        newan.ordernumber = self.ordernumber + 1
        newan.setXPos(self.getXPos())
        newan.setYPos(self.getYPos())
        self.getMyWorld().addToNewborns(newan)

    def action(self):
       #if self.huntTarget is None or self.huntTarget.isDead() is True:
        if 1:
            self.smellTarget()
        if self.huntTarget is not None:
            self.cyberaction()
        else:
            return super().action()

    def cyberaction(self):
        enemy: Organism = self.cybermove()
        if enemy is not None:
            return enemy.collision(self)
        else:
            return enemy

    def smellTarget(self):
        if self.getMyWorld().getNumberOfSosnowski() == 0:
            self.huntTarget = None
        else:
            sn: Organism
            mindist = self.getMyWorld().getBoardYSize()**2 * self.getMyWorld().getBoardXSize()**2
            iterator = 0
            minit = 0
            for sn in self.getMyWorld().sosnowskibucket:
                x = sn.getXPos() - self.getXPos()
                y = sn.getYPos() - self.getYPos()
                distance = x**2 + y**2
                if distance < mindist:
                    mindist = distance
                    minit = iterator
                iterator += 1
            self.huntTarget = self.getMyWorld().sosnowskibucket[minit]

    def cybermove(self):
        self.setLastXPos(self.getXPos())
        self.setLastYPos(self.getYPos())
        self.makecyberMove()
        enemy: Organism = self.myworld.getOrganismFromBoard(self.getXPos(), self.getYPos())
        return enemy

    def makecyberMove(self):
        targetX = self.huntTarget.getXPos()
        targetY = self.huntTarget.getYPos()
        nomove = True
        movedY = False
        movedX = False
        rng = randint(0, 1)
        if rng == 1:
            movedX = self.moveInX(targetX)
        if rng == 0:
            movedY = self.moveInY(targetY)
        if rng == 1 and movedX is False:
            self.moveInY(targetY)
        if rng == 0 and movedY is False:
            self.moveInX(targetX)


    def moveInX(self, targetX):
        if targetX > self.getXPos():
            self.setXPos(self.getXPos() + 1)
            return True
        elif targetX < self.getXPos():
            self.setXPos(self.getXPos() - 1)
            return True
        else:
            return False

    def moveInY(self, targetY):
        if targetY > self.getYPos():
            self.setYPos(self.getYPos() + 1)
            return True
        elif targetY < self.getYPos():
            self.setYPos(self.getYPos() - 1)
            return True
        else:
            return False