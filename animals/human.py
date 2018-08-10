from organisms import organism
from organisms.organism import Optional
from animals import animal
from world import World, Comentator
from random import randint

class Human(animal.Animal):
    def __init__(self, world: World, name: str) -> None:
        super().__init__(world, name)
        self.setType("HUMAN")
        self.setStrength(5)
        self.setInitiative(4)
        self.abilitycooldown = 0
        self.movedirection = 0
        self.cellcolor = "blue"

    def reproduce(self):
        return

    def getCooldown(self):
        return self.abilitycooldown

    def setMove(self, dir):
        self.movedirection = dir
        return

    def collision(self, enemy: organism.Organism):
        if self.isActiveSuperAbility() is False:
            return super().collision(enemy)
        else:
            if self.escapeFight() is True:
                return None
            else:
                return super().collision(enemy)

    def action(self):
        if self.isActiveSuperAbility() is False:
            enemy = super().action()
        else:
            enemy = self.move()
            if enemy is not None and enemy.getStrength() > self.getStrength():
                self.escapeFight()
            elif enemy is not None and enemy.getStrength() < self.getStrength():
                enemy = enemy.collision(self)
                self.decrementCooldown()
                if self.isActiveSuperAbility() is False:
                    self.setResistsPoison(False)
                return enemy
            enemy = None
        self.decrementCooldown()
        if self.isActiveSuperAbility() is False:
            self.setResistsPoison(False)
        Comentator.announceCooldown(self, self.myworld.getTextEditor())
        return enemy

    def isActiveSuperAbility(self):
        return self.abilitycooldown > 5

    def decrementCooldown(self):
        if self.abilitycooldown > 0:
            self.abilitycooldown -= 1

    def makeMove(self):
        if self.movedirection != 0:
            if self.movedirection == 1:
                if self.getYPos() > 0:
                    self.moveUp()
            if self.movedirection == 2:
                if self.getXPos() > 0:
                    self.moveLeft()
            if self.movedirection == 3:
                if self.getXPos() < self.myworld.getBoardXSize() - 1:
                    self.moveRight()
            if self.movedirection == 4:
                if self.getYPos() < self.myworld.getBoardYSize() - 1:
                    self.moveDown()

    def useSuperAbility(self):
        if self.abilitycooldown == 0:
            self.setResistsPoison(True)
            self.abilitycooldown = 11
