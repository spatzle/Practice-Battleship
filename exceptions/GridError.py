'''
Created on 2011-03-22

@author: joyce
'''
class GridError(Exception):

    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    
class GridSizeOutOfBound(GridError):
    def __init__(self):
        self.value = "grid cannot be too big or too small"
        
    def __str__(self):
        return repr(self.value)  