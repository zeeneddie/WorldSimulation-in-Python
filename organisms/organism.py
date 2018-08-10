from abc import ABC, abstractmethod
from world import World
from typing import Optional


class Organism(ABC):

    def __init__(self, world, name):
        super().__init__()
        self.cellcolor = ""
        self._lastxpos = 0
        self._lastypos = 0
        self._resistant_to_poison = False
        self._strength = 0
        self._initiative = 0
        self._xpos = 0
        self._ypos = 0
        self._age = 0
        self._newborn = 0
        self._name = name
        self._type = ""
        self._color = 0
        self._isdead = False
        self.myworld = world
        self.ordernumber = 0
        self.boardcell = None

    def getMyOrderNumber(self) -> int:
        return self.ordernumber

    def getLastXPos(self):
        return self._lastxpos
    def getLastYPos(self):
        return self._lastypos

    def isDead(self) -> int:
        return self._isdead

    def setAge(self, age):
        self._age = age

    def setResistsPoison(self, status):
        self._resistant_to_poison = status


    def isResistantToPoison(self):
        return self._resistant_to_poison

    def setType(self, mytype):
        self._type = mytype
        return

    def getType(self):
        return self._type

    @abstractmethod
    def action(self):
        return None

    def getStrength(self):
        return self._strength

    def setStrength(self, strength):
        self._strength = strength

    def getMyWorld(self) -> World:
        return self.myworld

    def getAge(self):
        return self._age

    def collision(self, enemy: 'Organism'):
        if enemy.getStrength() > self.getStrength():
            self.getMyWorld().killOrganism(self)
        elif enemy.getStrength() < self.getStrength():
            enemy.getMyWorld().killOrganism(enemy)
        else:
            if enemy.getAge() > self.getAge():
                self.getMyWorld().killOrganism(self)
            else:
                enemy.getMyWorld().killOrganism(enemy)
        return self

    def setXPos(self, xpos):
        self._xpos = xpos

    def setYPos(self, ypos):
        self._ypos = ypos

    def setLastXPos(self, xpos):
        self._lastxpos = xpos

    def setLastYPos(self, ypos):
        self._lastypos = ypos

    def cancelMove(self):
        self._xpos = self._lastxpos
        self._ypos = self._lastypos
        return

    def incrementAge(self):
        self._age += 1
        return

    def getColor(self):
        return self._color

    def makeDead(self):
        self._isdead = True

    def getInitative(self):
        return self._initiative

    def setInitiative(self, initiative):
        self._initiative = initiative

    def getXPos(self):
        return self._xpos

    def getYPos(self):
        return self._ypos

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def __eq__(self, other: 'Organism'):
        return self._name == other._name



