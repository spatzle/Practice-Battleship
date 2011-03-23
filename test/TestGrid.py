'''
Created on 2011-03-22

@author: joyce
'''
import unittest

from Grid import MyGrid, EnemyGrid
from GridError import GridSizeOutOfBound
from ShipError import ShipIsDiagonalError,\
    ShipPlacementSizeNotSameAsShipSizeError, ShipsOverLappedError
from Ship import Ship
from Point import Point
class TestGrid(unittest.TestCase):
    
    def testTooLargeGridOutOfBoundError(self):
        with self.assertRaises(GridSizeOutOfBound):
            EnemyGrid(16)
 
    def testTooSmallGridOutOfBoundError(self):
        with self.assertRaises(GridSizeOutOfBound):
            _ = MyGrid(-10)
            
    def testBoundNoGridOutOfBoundError(self):
            MyGrid(MyGrid.SZ_LARGE_BOUND)
            MyGrid(MyGrid.SZ_SM_BOUND)

    def testShipIsDiagonalError(self):
        with self.assertRaises(ShipIsDiagonalError):
            g = MyGrid()
            g.placeShipOnGrid(Ship(), Point([0,0]), Point([1,1]))

    def testShipPlacementSizeNotSameAsShipSizeError(self):
        with self.assertRaises(ShipPlacementSizeNotSameAsShipSizeError):
            g = MyGrid()
            g.placeShipOnGrid(Ship(),Point([0,0]),Point([0,3]))

    def testShipsOverlappedError(self):
        with self.assertRaises(ShipsOverLappedError):
                m = MyGrid()
                m.placeShipOnGrid(Ship(2,"dest","DE"), Point([1,1]), Point([2,1]))
                m.placeShipOnGrid(Ship(2,"dest","DE"), Point([1,1]), Point([2,1]))
                m.placeShipOnGrid(Ship(2,"dest","DE"), Point([3,3]), Point([3,4]))

if __name__ == '__main__':
    unittest.main()
    