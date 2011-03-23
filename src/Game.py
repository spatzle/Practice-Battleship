'''
Created on 2011-03-22

@author: joyce
'''
from Player import Player
from GameOver import GameOver
from PlayerError import FleetNotAllOnGrid
from Point import Point

def _setupPlayer(p,g):
    m = p.mygrid
    m.placeShipOnGrid(p.fleet.destroyer, Point([1,1]), Point([2,1]))
    m.placeShipOnGrid(p.fleet.submarine, Point([4,1]), Point([6,1]))
    m.placeShipOnGrid(p.fleet.cruiser, Point([2,3]), Point([2,5]))
    m.placeShipOnGrid(p.fleet.battleship, Point([6,5]), Point([9,5]))
    m.placeShipOnGrid(p.fleet.aircraftcarrier, Point([2,9]), Point([6,9]))
    print(m)
    try:
        p.ready()
    except FleetNotAllOnGrid:
        '''
        will try again
        '''    
        
class Game(object):
    
    
    isPlayer1Turn= True

    def __init__(self):
        self.player1 = Player("ATeam")
        self.player2 = Player("BTeam")
    
    def play(self):
        point = None
        while True:
            try:
                if(self.isPlayer1Turn):
                    hit=self.player1.mygrid.check(self.player1.fleet,point)
                    self.player2.enemygrid.update(point, hit)
                    point = self.player1.takeAGuess()
                    self.isPlayer1Turn = False
                else:
                    hit = self.player2.mygrid.check(self.player2.fleet,point)
                    self.player1.enemygrid.update(point, hit)
                    point = self.player2.takeAGuess()
                    self.isPlayer1Turn = True
            except GameOver:
                print(GameOver.value)
                if(self.isPlayer1Turn==True):
                    print(self.player1.teamName+" won")
                else: 
                    print(self.player2.teamName+" won")
                break
            
if __name__=='__main__':
    g = Game()
    _setupPlayer(g.player1,g)
    _setupPlayer(g.player2,g) 
    g.play()       