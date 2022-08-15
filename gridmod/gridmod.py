
class GridSpot:
    #Grid Spot; abbreviated for easier use
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
    #============================================#
    def left(self, grid):
        if self.x == 0:
            return GridSpot(self.x - 1, self.y, " ")
        for a in grid.gridspots:
            if a.x == self.x - 1 and a.y == self.y:
                return a
    #============================================#
    def right(self, grid):
        if self.x == grid.sizex:
            return GridSpot(self.x - 1, self.y, " ")
        for a in grid.gridspots:
            if a.x == self.x + 1 and a.y == self.y:
                return a
    #============================================#
    def top(self, grid):
        if self.y == grid.sizey:
            return GridSpot(self.x - 1, self.y, " ")
        for a in grid.gridspots:
            if a.x == self.x and a.y == self.y + 1:
                return a
    #============================================#
    def down(self, grid):
        if self.y == 0:
            return GridSpot(self.x - 1, self.y, " ")
        for a in grid.gridspots:
            if a.x == self.x and a.y == self.y - 1:
                return a
    #============================================#
    def changeValue(self, newvalue):
        self.value = newvalue
    #============================================#
    def convertToVisual(self):
        return "["+self.value+"]"
    #============================================#
    def convertToVisualClean(self):
        return self.value+'  '
    
class Area:
    def __init__(self, areaspots):
        self.areaspots = areaspots
    def convertTo(self, value):
        for a in self.areaspots:
            a.changeValue(value)

class Grid:
    def __init__(self, gridspots, sizex, sizey):
        self.gridspots = gridspots
        self.sizex = int(sizex)
        self.sizey = int(sizey)
    #============================================#
    def getspot(self, x, y):
        for a in self.gridspots:
            if a.x == x and a.y == y:
                return a
        return GridSpot(x, y, " ")
    #============================================#
    def convertToVisual(self):
        griddict = {}
        for a in range(0, self.sizey):
            griddict[a] = []
        for a in self.gridspots:
            griddict[a.y].append(a.convertToVisual())
        return griddict
    #============================================#
    def printSelf(self):
        griddict = {}
        for a in range(0, self.sizey):
            griddict[a] = []
        for a in self.gridspots:
            griddict[a.y].append(a.convertToVisual())
        for a in griddict:
            string = ""
            for b in griddict[a]:
                string += b
            print(string)
    #============================================#
    def printSelfClean(self):
        griddict = {}
        for a in range(0, self.sizey):
            griddict[a] = []
        for a in self.gridspots:
            griddict[a.y].append(a.convertToVisualClean())
        for a in griddict:
            string = ""
            for b in griddict[a]:
                string += b
            print(string)
    #============================================#
    def convertTo(self, value):
        for a in self.gridspots:
            a.value = value
    #============================================#
    def getarea(self, x1,y1,x2,y2):
        area = []
        for a in self.gridspots:
            if(a.x>=x1 and a.y>=y1 and a.x<=x2 and a.y<=y2):
                area.append(a)
        return Area(area)


def createGrid(sizex, sizey, value = ' '):
    ID = 0
    gridx = {}
    for x in range(0, int(sizex)):
        for y in range(0, int(sizey)):
            gridx[ID] = GridSpot(x,y, value)
            ID += 1
    gridlist = []
    for a in gridx:
        gridlist.append(gridx[a])
    grid = Grid(gridlist, sizex, sizey)
    return grid