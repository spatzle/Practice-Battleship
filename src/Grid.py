'''
Created on 2011-03-22

@author: joyce
'''
from GridError import GridSizeOutOfBound
from ShipError import ShipIsDiagonalError,\
    ShipPlacementSizeNotSameAsShipSizeError, ShipsOverLappedError
from Ship import Ship
from Point import Point
import re
from GameOver import GameOver

class Grid(object):
    SZ_SM_BOUND=10
    SZ_LARGE_BOUND=15
    isMyGrid = True
    
    '''
    classdocs
    '''
    def _newCol_(self,x):
        a = []
        for y in range(0,self.size):
            if(self.isMyGrid==False):
                a.append(-1)
            else: a.append("("+str(x)+","+str(y)+")")
        return a
            
    def __init__(self,size,isMyGrid):
        if size<self.SZ_SM_BOUND or size > self.SZ_LARGE_BOUND: raise GridSizeOutOfBound
        self.size = size
        self.grid = []
        self.isMyGrid = isMyGrid
        for y in range(0,self.size):
            self.grid.append(self._newCol_(y))

    def __str__(self):
        s = ""
        for y in range(0,self.size):
            for x in range (0,self.size):
                if x!=0:s +=","
                s += str(self.grid[x][y])
            s +="\n"
        return s      
        
class MyGrid(Grid):
    def check(self,fleet,point):
        '''
        1. see if correct
            return the answer           
        2. see if all ships sunk, if so raise GameOver
        '''
        hit = None
        if re.match("[A-Z]", self.grid[point.x][point.y]) :
            hit = self.grid[point.x][point.y]
            fleet.FLEET_CODES[hit].hit
        if fleet.isSunk():
            raise GameOver
        if not hit==None:
            return 1
        else: return 0
        
    def placeShipOnGrid(self,ship,head,tail):
        sameRow = sameCol =False
        placementLength = 0
        if tail.x -head.x ==0: 
            sameCol =True 
            placementLength = tail.y-head.y +1
        elif tail.y-head.y==0: 
            sameRow = True
            placementLength = tail.x-head.x+1
        if sameRow!=True and sameCol!=True: raise  ShipIsDiagonalError
        if abs(placementLength) != ship.size:
            print(placementLength)
            raise ShipPlacementSizeNotSameAsShipSizeError
        if placementLength <0:
            temp = tail
            tail = head
            head = temp
            placementLength *= -1
        head.isHead=True
        
        if sameRow==True: 
            for i in range(0,tail.x-head.x+1):
                if not re.match("\(.+\)", self.grid[head.x+i][head.y]) :
                    raise ShipsOverLappedError
                self.grid[head.x+i][head.y] = " "+ship.shortform[i]+"   "                
        else:
            for i in range(0,tail.y-head.y+1):
                if not re.match("\(.+\)", self.grid[head.x][head.y+i]) :
                    raise ShipsOverLappedError
                self.grid[head.x][head.y+i] = " "+ship.shortform[i]+"   "
        ship.isOnGrid = True
        
    def __init__(self,size=10):
        Grid.__init__(self,size,True)
        self.isMyGrid = True

class EnemyGrid(Grid):
    def update(self,point,correctness=0):
        self.grid[point.x][point.y]=correctness
        
    def __init__(self,size=10):
        Grid.__init__(self,size,False)

if __name__ == '__main__':
    g = EnemyGrid()
    print(g)
    m = MyGrid()
    m.placeShipOnGrid(Ship(2,"dest","DE"), Point([1,1]), Point([2,1]))
    print(m)      