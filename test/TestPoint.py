'''
Created on 2011-03-22

@author: joyce
'''
import unittest

from Point import Point
from PointError import PointOutOfBoundError

class TestPoint(unittest.TestCase):
    
    def testPointOutOfBoundError(self):
        with self.assertRaises(PointOutOfBoundError):
            p = Point(1,-2)


if __name__ == '__main__':
    unittest.main()
    
