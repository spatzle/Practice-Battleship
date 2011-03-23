'''
Created on 2011-03-22

@author: joyce
'''
from Ship import *
from unittest.test import support
class Fleet(object):
    '''
    classdocs
    '''
    destroyer = submarine= cruiser = battleship = aircraftcarrier = None
    FLEET_CODES={
               "D":destroyer
               ,"S":submarine
               ,"C":cruiser
               ,"B":battleship
               ,"A":aircraftcarrier
               }

    def __init__(self):
        '''
        Constructor
        '''
        self.destroyer = Destroyer()
        self.submarine = Submarine()
        self.cruiser = Cruiser()
        self.battleship = BattleShip()
        self.aircraftcarrier = AircraftCarrier()
        
    def isSunk(self):
        count=0
        for ship in self.FLEET_CODE.iterkeys():
            if ship.isSunk:
                count+=1
        if count == len(self.FLEET_CODES):
            return True
        return False
        