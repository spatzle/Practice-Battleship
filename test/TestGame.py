'''
Created on 2011-03-22

@author: joyce
'''
import unittest
from Player import Player
from Point import Point
from PlayerError import FleetNotAllOnGrid
from Game import Game

class TestGame(unittest.TestCase):
    def _setupPlayer(self,p,g):
        m = p.mygrid
        m.placeShipOnGrid(p.fleet.destroyer, Point([1,1]), Point([2,1]))
        m.placeShipOnGrid(p.fleet.submarine, Point([4,1]), Point([6,1]))
        m.placeShipOnGrid(p.fleet.cruiser, Point([2,3]), Point([2,5]))
        m.placeShipOnGrid(p.fleet.battleship, Point([6,5]), Point([9,5]))
        m.placeShipOnGrid(p.fleet.aircraftcarrier, Point([2,9]), Point([6,9]))
        print(m)
        try:
            p.ready()
        except FleetNotAllOnGrid:
            '''
            will try again
            '''

    def testGameOk(self):
        g = Game()
        self._setupPlayer(g.player1,g)
        self._setupPlayer(g.player2,g) 
        g.play()       
        

if __name__ == '__main__':
    unittest.main()    
    
