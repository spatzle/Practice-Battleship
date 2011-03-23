'''
Created on 2011-03-22

@author: joyce
'''
class PlayerError(Exception):

    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    


class PointsOverlapsError(PlayerError):
    def __init__(self):
        self.value = "Points are overlapping"

class FleetNotAllOnGrid(PlayerError):
    def __init__(self):
        self.value = "Fleet ships not all on grid"        