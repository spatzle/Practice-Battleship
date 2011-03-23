'''
Created on 2011-03-22

@author: joyce
'''
from PointError import PointOutOfBoundError

class Point(object):
    '''
    classdocs
    '''

    def __init__(self,xyCoords):
        if xyCoords[0]<0 or xyCoords[1]<0: 
            raise PointOutOfBoundError()
        self.x = xyCoords[0]
        self.y = xyCoords[1]    
        self.isHead=False
    
    def __str__(self):
        s= "x "+str(self.x)+" y "+str(self.y)+"."
        return s
        