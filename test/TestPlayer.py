'''
Created on 2011-03-22

@author: joyce
'''
import unittest
from Player import Player
from Point import Point
from PlayerError import FleetNotAllOnGrid
class TestPlayer(unittest.TestCase):
    

    def testFleetNotAllOnGridError(self):
        with self.assertRaises(FleetNotAllOnGrid):
            g = Player()
            m = g.mygrid
            m.placeShipOnGrid(g.fleet.destroyer, Point([1,1]), Point([2,1]))
            m.placeShipOnGrid(g.fleet.submarine, Point([4,1]), Point([6,1]))
            m.placeShipOnGrid(g.fleet.cruiser, Point([2,3]), Point([2,5]))
            m.placeShipOnGrid(g.fleet.battleship, Point([6,5]), Point([9,5]))
#            m.placeShipOnGrid(g.fleet.aircraftcarrier, Point([2,9]), Point([6,9]))
            print(m)
            g.ready()

if __name__ == '__main__':
    unittest.main()    
    
