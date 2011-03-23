'''
Created on 2011-03-22

@author: joyce
'''
import unittest
from ShipError import ShipOutOfBoundError
from Ship import Ship

class TestShip(unittest.TestCase):
    
    def testShipOutOfBoundError(self):
        with self.assertRaises(ShipOutOfBoundError):
            s = Ship(1)
            
if __name__ == '__main__':
    unittest.main()    
    
