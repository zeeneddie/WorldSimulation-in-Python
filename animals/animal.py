from organisms import organism
from organisms.organism import  Optional
from random import randint
from abc import ABC, abstractmethod


class Animal(organism.Organism):

    def __init__(self, world, name):
        super().__init__(world, name)
        self.setResistsPoison(False)

    def action(self) -> Optional[organism.Organism]:
        enemy: organism = self.move()
        if enemy is not None:
            return enemy.collision(self)
        else:
            return enemy

    def move(self) -> Optional[organism.Organism]:
        self.setLastXPos(self.getXPos())
        self.setLastYPos(self.getYPos())
        self.makeMove()
        enemy: organism.Organism = self.myworld.getOrganismFromBoard(self.getXPos(), self.getYPos())
        return enemy

    def collision(self, enemy: organism.Organism) -> Optional[organism.Organism]:
        if enemy.getType() == self.getType():
            if enemy.getAge() > 10 and self.getAge() > 10:
                enemy.cancelMove()
                self.reproduce()
                return None
            else:
                enemy.cancelMove()
                return None
        else:
            return super().collision(enemy)

    def escapeFight(self) -> bool:
        freespotsY = []
        freespotsX = []
        iterator = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= self.getXPos() + i <= self.myworld.getBoardXSize() - 1:
                    if 0 <= self.getYPos() + j <= self.myworld.getBoardYSize() - 1:
                        enemy = self.myworld.getOrganismFromBoard(self.getXPos() + i, self.getYPos() + j)
                        if enemy is None:
                            freespotsY.append(j+self.getYPos())
                            freespotsX.append(i+self.getXPos())
                            iterator += 1

        if iterator > 0:
            rng = randint(0, iterator - 1)
            self.setLastYPos(self.getYPos())
            self.setLastXPos(self.getXPos())
            self.setXPos(freespotsX[rng])
            self.setYPos(freespotsY[rng])
            return True
        else:
            return False

    @abstractmethod
    def reproduce(self):
        pass

    def makeMove(self):
        didmove = False
        iterator = 0
        while didmove is False and iterator < 1000:
            rng = randint(0, 3)
            iterator += 1
            didmove = False
            if rng == 0:
                if self.getYPos() > 0:
                    self.moveUp()
                    didmove = True
            if rng == 1:
                if self.getXPos() > 0:
                    self.moveLeft()
                    didmove = True
            if rng == 2:
                if self.getXPos() < self.myworld.getBoardXSize() - 1:
                    self.moveRight()
                    didmove = True
            if rng == 3:
                if self.getYPos() < self.myworld.getBoardYSize() - 1:
                    self.moveDown()
                    didmove = True

    def moveUp(self):
        self.setYPos(self.getYPos() - 1)

    def moveDown(self):
        self.setYPos(self.getYPos() + 1)

    def moveRight(self):
        self.setXPos(self.getXPos() + 1)

    def moveLeft(self):
        self.setXPos(self.getXPos() - 1)


