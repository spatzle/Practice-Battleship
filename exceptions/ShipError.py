'''
Created on 2011-03-22

@author: joyce
'''
class ShipError(Exception):

    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    
class ShipOutOfBoundError(ShipError):
    def __init__(self):
        self.value = "Ship size out of bound"

class ShipIsDiagonalError(ShipError):
    def __init__(self):
        self.value = "Ship cannot be diagonal"

class ShipPlacementSizeNotSameAsShipSizeError(ShipError):
    def __init__(self):
        self.value = "Ship size need to be same as placement's length"

class ShipsOverLappedError(ShipError):
    def __init__(self):
        self.value = "Ships cannot overlap"
