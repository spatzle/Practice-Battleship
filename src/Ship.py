'''
Created on 2011-03-22

@author: joyce
'''
from ShipError import ShipOutOfBoundError

class Ship(object):
    SIZES=(2,3,4,5)

    def __init__(self,size=2,name="aShip"
                 ,shortform="S",code="S"):
        if size not in self.SIZES:
            raise ShipOutOfBoundError
        self.name = name
        self.size = size
        self.shortform = shortform
        self.isOnGrid = False
        self.isSunk = False
        self.hitTimes=0
        self.code = code
        
    def hit(self):
        self.hitTimes+=1
        if (self.hitTimes)==self.size:
            self.isSunk=True

class Destroyer(Ship):
    def __init__(self):
        Ship.__init__(self,2,"Destroyer","DS","D")

class Submarine(Ship):
    def __init__(self):
        Ship.__init__(self,3,"Submarine","SUB","S")

class Cruiser(Ship):
    def __init__(self):
        Ship.__init__(self,3,"Cruiser","CRU","C")
        
class BattleShip(Ship):
    def __init__(self):
        Ship.__init__(self,4,"BattleShip","BATT","B")

class AircraftCarrier(Ship):
    def __init__(self):
        Ship.__init__(self,5,"AircraftCarrier","CARRI","A")
