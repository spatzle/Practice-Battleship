'''
Created on 2011-03-22

@author: joyce
'''
from Grid import MyGrid,EnemyGrid
from Fleet import Fleet
from PlayerError import  FleetNotAllOnGrid
from Point import Point
from MadeAGuess import Guess
import re
from GameOver import GameOver
from Utils import matched
from PointError import PointError
class Player(object):

    def __init__(self,teamName="ATeam"):
        self.mygrid = MyGrid()
        self.enemygrid = EnemyGrid()
        self.fleet = Fleet()
        self.teamName = teamName

    def ready(self):
        ready = (self.fleet.submarine.isOnGrid 
        and self.fleet.destroyer.isOnGrid
        and self.fleet.cruiser.isOnGrid
        and self.fleet.battleship.isOnGrid
        and self.fleet.aircraftcarrier.isOnGrid)
        if not ready: raise FleetNotAllOnGrid
        else: return ready


    def getInput(self,msg=""):
        x = None
        while not x:
            x = str(input(msg+"\nTake a guess, "+self.teamName+" Guesses must be of format (0,0):"))
        return x

    def takeAGuess(self):
        msg = ""
        point = None
        while True:
            input = str(self.getInput(msg)).strip()
            # parse input
            patt = re.compile(r'(\d+,\d+)')
            if patt.search(input)==None:
                msg="Bad input, try again. "
            else:
                splitted = re.split(",", input)
                try:
                    point = Point([int(splitted[0][1:]),int(splitted[1][:len(splitted[1])-1])])
                except PointError:
                    print("you forfeit your turn by making silly guesses")
                break
        return point
            