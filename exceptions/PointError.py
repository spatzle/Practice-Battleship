'''
Created on 2011-03-22

@author: joyce
'''
class PointError(Exception):

    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    
class PointOutOfBoundError(PointError):
    def __init__(self):
        self.value = "point is out of bound"
        
    def __str__(self):
        return repr(self.value)  