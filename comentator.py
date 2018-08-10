from PyQt5 import QtWidgets


class Comentator():
    def __init__(self):
        return

    @staticmethod
    def announceMove(org, te: QtWidgets.QTextEdit):
        te.append(org.getName()+" MOVED TO x:"+str(org.getXPos()) + " y:"+str(org.getYPos()))
        return

    @staticmethod
    def separator(te: QtWidgets.QTextEdit):
        te.append("-------------------------------------")
        return

    @staticmethod
    def announceDeath(died, te: QtWidgets.QTextEdit):
        te.append(died.getName()+"died at x:"+str(died.getXPos())+" y:"+str(died.getYPos()))
        return

    @staticmethod
    def writeOrgInfo(org, te: QtWidgets.QTextEdit):
        if org is not None:
            te.append("x: "+str(org.getYPos())+"y:"+str(org.getXPos())+"isdead:"+str(org.isDead())+"name:"+str(org.getName())+"type"+str(org.getType()))
        return

    @staticmethod
    def announceCooldown(org, te: QtWidgets.QPushButton):
        te.append("cd: " + str(org.getCooldown()))
