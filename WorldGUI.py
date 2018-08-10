from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QApplication, qApp, QFileDialog
from PyQt5.QtCore import Qt
from Ui_MainWindow import Ui_MainWindow
from world import World, Comentator
from organisms.organism import Organism
from animals.wolf import Wolf
from animals.turtle import Turtle
from animals.sheep import Sheep
from animals.wolf import Wolf
from animals.antelope import Antelope
from plants.dandelion import Dandelion
from plants.deadlynightshade import DeadlyNightshade
from plants.grass import Grass
from plants.guarana import Guarana
from plants.heracleumsosnowskyi import Sosnowski
from animals.fox import Fox
from animals.cybersheep import CyberSheep
from animals.human import Human


class customQPushButton(QtWidgets.QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.myorg = None


class UIMAIN(QMainWindow, Ui_MainWindow):
    def __init__(self, world: World):
        super(UIMAIN, self).__init__()
        self.setupUi(self)
        self.myworld: World = world
        for i in range(0, world.BoardYSize):
            for j in range(0, world.BoardXSize):
                world.boardbuttons[i][j]: QtWidgets.QPushButton = customQPushButton(self.gridLayoutWidget)
                world.boardbuttons[i][j].setEnabled(True)
                world.boardbuttons[i][j].setObjectName("CellButtonnr"+str(i)+str(j))
                world.boardbuttons[i][j].setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
                self.gridLayout.addWidget(world.boardbuttons[i][j], i, j, 1, 1)
                world.boardbuttons[i][j].setStyleSheet("background-color: white")
                world.boardbuttons[i][j].clicked.connect(lambda: self.buttonClicked())

        self.savebt.clicked.connect(lambda: self.saveGame())
        self.loadbt.clicked.connect(lambda: self.loadGame())
        self.pushButton.clicked.connect(lambda: self.myworld.endTurn())
        self.pushButton.clicked.connect(lambda: self.lcdNumber.display(self.myworld.turncounter))
        self.show()


    def saveGame(self):
        fname: str = QFileDialog.getOpenFileName(self, 'Open file')
        if fname[0] is "":
            return
        file = open(fname[0], 'w')
        file.write(str(self.myworld.getBoardYSize())+"\n")
        file.write(str(self.myworld.getBoardXSize())+"\n")
        file.write(str(self.myworld.getNumberOfOrganisms())+"\n")
        file.write(str(self.myworld.turncounter)+"\n")
        org: Organism
        for org in self.myworld.organismsqueue:
            file.write(str(org.getType())+"\n")
            file.write(str(org.getXPos())+"\n")
            file.write(str(org.getYPos())+"\n")
            file.write(str(org.isResistantToPoison())+"\n")
            file.write(str(org.getLastXPos())+"\n")
            file.write(str(org.getLastYPos())+"\n")
            file.write(str(org.getStrength())+"\n")
            file.write(str(org.getInitative())+"\n")
            file.write(str(org.getAge())+"\n")
            file.write(str(org.getName())+"\n")
            ###BRAKUJE TU KILKU KTORE BYLY W JAVIE
            file.write(str(org.isDead())+"\n")
        file.close()

    def loadGame(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        if fname[0] is "":
            return
        file = open(fname[0], 'r')
        sizeX = int(file.readline())
        sizeY = int(file.readline())
        for i in range(0, sizeY):
            for j in range(0, sizeX):
                self.myworld.boardbuttons[i][j].setStyleSheet("background-color: white")
                self.myworld.boardbuttons[i][j].myorg = None
                self.myworld.boardbuttons[i][j].setText(QtCore.QCoreApplication.translate("MainWindow", ""))
        self.myworld.resetWorld(sizeX, sizeY)
        numorg = int(file.readline())
        tc = int(file.readline())
        self.myworld.turncounter = tc
        for i in range(0, numorg):
            thetype = str(file.readline())
            thetype = thetype.rstrip()
            neworg = self.organismChooseByType(thetype)
            xpos = int(file.readline())
            ypos = int(file.readline())
            self.myworld.addOrganismWithCords(neworg, xpos, ypos)
            if thetype == 'HUMAN' or thetype == "HUMAN":
                self.myworld.human = neworg
            res = file.readline()
            res = res.strip()
            if res == 'True':
                res = True
            elif res == 'False':
                res = False
            neworg.setResistsPoison(res)
            neworg.setLastXPos(int(file.readline()))
            neworg.setLastYPos(int(file.readline()))
            neworg.setStrength(int(file.readline()))
            neworg.setInitiative(int(file.readline()))
            neworg.setAge(int(file.readline()))
            neworg.setName(file.readline().strip('\n'))
            isdead = file.readline()
            isdead = isdead.strip()
            if isdead == 'True':
                isdead = True
            elif isdead == 'False':
                isdead = False
            if isdead is True:
                neworg.makeDead()
        file.close()



    def keyPressEvent(self, e):
        if e.key() == Qt.Key_E:
            self.myworld.endTurn()
            self.lcdNumber.display(self.myworld.turncounter)
        if e.key() == Qt.Key_Q:
            self.close()
        if e.key() == Qt.Key_W:
            self.myworld.human.movedirection = 1
            self.myworld.endTurn()
            self.lcdNumber.display(self.myworld.turncounter)
        if e.key() == Qt.Key_S:
            self.myworld.human.movedirection = 4
            self.myworld.endTurn()
            self.lcdNumber.display(self.myworld.turncounter)
        if e.key() == Qt.Key_D:
            self.myworld.human.movedirection = 3
            self.myworld.endTurn()
            self.lcdNumber.display(self.myworld.turncounter)
        if e.key() == Qt.Key_A:
            self.myworld.human.movedirection = 2
            self.myworld.endTurn()
            self.lcdNumber.display(self.myworld.turncounter)
        if e.key() == Qt.Key_R:
            self.myworld.human.useSuperAbility()
            self.myworld.endTurn()
            self.lcdNumber.display(self.myworld.turncounter)

    def buttonClicked(self):
        bt: QtWidgets.QPushButton = self.sender()
        if self.myworld.te is not None and bt.myorg is not None:
            self.myworld.te.append("type:" + bt.myorg.getType())
            self.myworld.te.append("name:" + bt.myorg.getName())
            if bt.myorg in self.myworld.organismsqueue:
                self.myworld.te.append("in orgque")
        else:
            idx = self.gridLayout.indexOf(bt)
            location = self.gridLayout.getItemPosition(idx)
            _type = self.showDialog()
            org2add = self.organismChooseByType(_type)
            if org2add is not None:
                self.myworld.addOrganismWithCords(org2add, location[1], location[0])
            else:
                self.myworld.te.append("None")

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Animal choose', 'Enter animal type:')
        if ok:
            return text
        else:
            return None

    def organismChooseByType(self, _type):
            if _type == 'FOX':
                return Fox(self.myworld, "fo1"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            if _type == 'ANTELOPE':
                return Antelope(self.myworld, "at1"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            if _type == 'HUMAN':
                return Human(self.myworld, "h1"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            if _type == 'SHEEP':
                return Sheep(self.myworld, "s1"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            if _type == 'TURTLE':
                return Turtle(self.myworld, "t1"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            if _type == 'WOLF':
                return Wolf(self.myworld, "w1"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            if _type == 'DANDELION':
                return Dandelion(self.myworld, "d1"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            if _type == 'DEADLYNIGHTSHADE':
                return DeadlyNightshade(self.myworld, "dst1"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            if _type == 'GUARANA':
                return Guarana(self.myworld, "gr1"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            if _type == 'SOSNOWSKI':
                return Sosnowski(self.myworld, "sns1"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            if _type == 'GRASS':
                return Grass(self.myworld, "gr1"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            if _type == 'CYBERSHEEP':
                return CyberSheep(self.myworld, "cb2"+str(self.myworld.getNumberOfOrganisms())+"n"+str(self.myworld.turncounter))
            else:
                return None