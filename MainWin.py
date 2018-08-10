import sys
from PyQt5.QtWidgets import QApplication
from world import World, Comentator
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
from animals.human import Human
from animals.cybersheep import CyberSheep
from WorldGUI import UIMAIN


if __name__ == '__main__':
    app = QApplication(sys.argv)
    newcomentator = Comentator()
    world = World(None, newcomentator, 20, 20)
    ex = UIMAIN(world)
    hm = Human(world, "HUMAN")
    world.addOrganism(hm)
    world.human = hm
    for i in range(0, 1):
        world.addOrganism(Sosnowski(world, "SOS1"+str(i)))
        world.addOrganism(CyberSheep(world, "CB1"+str(i)))
        world.addOrganism(Grass(world, "G1" + str(i)))
        world.addOrganism(Dandelion(world, "DND1"+str(i)))
        world.addOrganism(Guarana(world, "GU1"+str(i)))
        world.addOrganism(Antelope(world, "ANT1" + str(i)))
        world.addOrganism(Grass(world, "G1" + str(i)))
        world.addOrganism(Fox(world, "F1"+str(i)))
        world.addOrganism(Wolf(world, "WLF1"+str(i)))
        world.addOrganism(DeadlyNightshade(world, "DN1"+str(i)))
        world.addOrganism(Sheep(world, "SH1"+str(i)))
        world.addOrganism(Turtle(world, "TRTL1"+str(i)))
    world.linkTextEditor(ex.textEdit)
    sys.exit(app.exec_())


