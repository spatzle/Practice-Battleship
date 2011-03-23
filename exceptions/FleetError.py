'''
Created on 2011-03-22

@author: joyce
'''
class FleetError(Exception):

    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    
