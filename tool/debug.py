from enum import Enum


class STACK(Enum):
    IN = 1
    OUT = 2
    STATE = 3


class debugTool:

    def __init__(self):
        self.nTab = -1

    def setnTab(self, stack=STACK.STATE):
        if stack == STACK.IN:
            self.nTab += 1
        if stack == STACK.OUT:
            self.nTab -= 1

    def printWithTab(self, val):
        if self.nTab == 0:
            a = 0
        print("|"+"   |" * self.nTab + str(val))
