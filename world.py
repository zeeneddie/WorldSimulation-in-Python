from operator import attrgetter
from random import randint
from comentator import Comentator, QtWidgets
from PyQt5 import  QtCore


class World:
    def __init__(self, human, comentator, xsize, ysize):
        self.BoardXSize = xsize
        self.BoardYSize = ysize
        self.boardbuttons: QtWidgets.QPushButton = [[None for x in range(xsize)] for y in range(ysize)]
        self.human = human
        self.organismsqueue = []
        self.sosnowskibucket = []
        self.comentator = comentator
        self.deadorganisms = []
        self.te = None
        self.numofSosnowski = 0
        self.turncounter = 0
        self.newborns = []
        self.organismsboard = [[None for x in range(xsize)] for y in range(ysize)]
        self.numberoforganisms = 0

    def resetWorld(self, xsize, ysize):
        self.deadorganisms.clear()
        self.newborns.clear()
        self.organismsqueue.clear()
        self.organismsboard = [[None for x in range(xsize)] for y in range(ysize)]
        self.BoardXSize = xsize
        self.BoardYSize = ysize
        self.human = None


    def linkTextEditor(self, te: QtWidgets.QTextEdit):
        self.te = te

    def getTextEditor(self):
        return self.te

    def getBoardXSize(self) -> int:
        return self.BoardXSize

    def getBoardYSize(self) -> int:
        return self.BoardYSize

    def getOrganismFromBoard(self, x, y):
        return self.organismsboard[x][y]

    def setOrganismOnBoard(self, x, y, organism):
        self.organismsboard[x][y] = organism

    def isBoardCellFree(self, x, y):
        if self.organismsboard[x][y] is None:
            return True
        else:
            return False

    def getNumberOfSosnowski(self):
        return self.numofSosnowski

    def getNumberOfOrganisms(self):
        return self.numberoforganisms

    def getOrganisms(self):
        return self.organismsboard

    def sortOrganisms(self, mylist):
        mylist.sort(key=attrgetter("_initiative", "_age"), reverse=True)

    def addToNewborns(self, nb):
        self.newborns.append(nb)

    def addToDeadOrganisms(self, do):
        self.deadorganisms.append(do)


    def addOrganism(self, organism):
        if self.getNumberOfOrganisms() < self.BoardYSize * self.BoardXSize:
            while True:
                x = randint(0, self.getBoardXSize()-1)
                y = randint(0, self.getBoardYSize()-1)
                if self.isBoardCellFree(x, y) is True:
                    break
            organism.setXPos(x)
            organism.setYPos(y)
            organism.setLastXPos(x)
            organism.setLastYPos(y)
            organism.ordernumber += 1
            self.organismsboard[x][y] = organism
            self.organismsqueue.append(organism)
            self.sortOrganisms(self.organismsqueue)
            self.numberoforganisms += 1
            organism.boardcell: QtWidgets.QPushButton = self.boardbuttons[y][x]
            organism.boardcell.setStyleSheet("background-color: "+organism.cellcolor)
            organism.boardcell.setText(QtCore.QCoreApplication.translate("MainWindow", "anim"))
            organism.boardcell.myorg = organism
            if organism.getType() == "SOSNOWSKI":
                self.numofSosnowski += 1
                self.sosnowskibucket.append(organism)
            return True
        else:
            return False

    def addBaby(self, baby):
        if self.getNumberOfOrganisms() < self.BoardYSize * self.BoardXSize:
            freespotsY = []
            freespotsX = []
            iterator = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if baby.getXPos() + i >= 0 and baby.getXPos() + i <= self.getBoardXSize() - 1 and baby.getYPos() + j >= 0 and baby.getYPos() + j <= self.getBoardYSize() - 1:
                        enemy = self.getOrganismFromBoard(baby.getXPos() + i, baby.getYPos() + j)
                        if enemy is None:
                            freespotsY.append(j + baby.getYPos())
                            freespotsX.append(i + baby.getXPos())
                            iterator += 1
            if iterator > 0:
                rng = randint(0, iterator - 1)
                baby.setXPos(freespotsX[rng])
                baby.setYPos(freespotsY[rng])
                baby.setLastYPos(freespotsY[rng])
                baby.setLastXPos(freespotsX[rng])
                baby.boardcell: QtWidgets.QPushButton = self.boardbuttons[baby.getYPos()][baby.getXPos()]
                baby.boardcell.setStyleSheet("background-color: " + baby.cellcolor)
                baby.boardcell.setText(QtCore.QCoreApplication.translate("MainWindow", "anim"))
                baby.boardcell.myorg = baby
                baby.ordernumber += 1
            else:
                return False
            self.organismsboard[baby.getXPos()][baby.getYPos()] = baby
            self.organismsqueue.append(baby)
            self.numberoforganisms += 1
            if baby.getType() == "SOSNOWSKI":
                self.numofSosnowski += 1
                self.sosnowskibucket.append(baby)
            return True
        else:
            return False

    def addOrganismWithCords(self, organism, x, y):
        organism.setXPos(x)
        organism.setYPos(y)
        organism.setLastXPos(x)
        organism.setLastYPos(y)
        self.organismsboard[x][y] = organism
        self.organismsqueue.append(organism)
        self.sortOrganisms(self.organismsqueue)
        self.numberoforganisms += 1
        organism.boardcell: QtWidgets.QPushButton = self.boardbuttons[y][x]
        organism.boardcell.setStyleSheet("background-color: " + organism.cellcolor)
        organism.boardcell.setText(QtCore.QCoreApplication.translate("MainWindow", "anim"))
        organism.boardcell.myorg = organism
        if organism.getType() == "SOSNOWSKI":
            self.numofSosnowski += 1
            self.sosnowskibucket.append(organism)

    def deleteOrganism(self, organism):
        self.organismsboard[organism.getXPos()][organism.getYPos()] = None
        if organism in self.organismsqueue:
            if organism.getType() == "SOSNOWSKI":
                self.numofSosnowski -= 1
                self.sosnowskibucket.remove(organism)
            self.organismsqueue.remove(organism)
            return True
        else:
            return False



    def endTurn(self):
        for org in self.organismsqueue:
            self.organismsboard[org.getXPos()][org.getYPos()] = None
            if org.isDead() is False:
                org.boardcell.setStyleSheet("background-color: white")
                org.boardcell.setText(QtCore.QCoreApplication.translate("MainWindow", ""))
                org.boardcell.myorg = None
                org.boardcell = None
                org.action()
                Comentator.announceMove(org, self.te)
                if org.isDead() is False:
                    self.organismsboard[org.getXPos()][org.getYPos()] = org
                    org.boardcell = self.boardbuttons[org.getYPos()][org.getXPos()]
                    org.boardcell.setStyleSheet("background-color: "+org.cellcolor)
                    org.boardcell.setText(QtCore.QCoreApplication.translate("MainWindow", org._name))
                    org.boardcell.myorg = org
        for org in self.organismsqueue:
            org.incrementAge()
        for do in self.deadorganisms:
            if do.getType() == "SOSNOWSKI":
                self.numofSosnowski -= 1
                self.sosnowskibucket.remove(do)
            self.organismsqueue.remove(do)
            self.numberoforganisms -= 1
        for nb in self.newborns:
            self.addBaby(nb)
        self.deadorganisms.clear()
        self.newborns.clear()
        Comentator.separator(self.te)
        self.sortOrganisms(self.organismsqueue)
        self.turncounter += 1
        self.human.movedirection = 0

    def killOrganism(self,  org):
        org.makeDead()
        self.organismsboard[org.getXPos()][org.getYPos()] = None
        if org.boardcell is not None:
            org.boardcell.setStyleSheet("background-color: white")
            org.boardcell.setText(QtCore.QCoreApplication.translate("MainWindow", ""))
            org.boardcell.myorg = None
        org.boardcell = None
        Comentator.announceDeath(org, self.te)
        if org not in self.deadorganisms:
            self.deadorganisms.append(org)

    def deleteOrganismFromBoard(self, x, y):
        self.organismsboard[x][y] = None


