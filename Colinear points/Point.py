import matplotlib.pyplot as plt
from Comparator import Comparator

class IPoint:

    def draw(self)->None:
        """ # draws this point"""    

    def drawTo(self, that)->None:       
        """# draws the line segment from this point to that point"""        

    # compare two points by y-coordinates, breaking ties by x-coordinates
    def compareTo(self, that)->int:
        """The compareTo() method should compare points by their y-coordinates, breaking ties by their x-coordinates. 
        Formally, the invoking point (x0, y0) is less than the argument point (x1, y1) if and only if either y0 < y1 or if y0 = y1 and x0 < x1."""
    
    # the slope between this point and that point
    def slopeTo(self, that)->float:
        """Treat the slope of a horizontal line segment as positive zero; treat the slope of a vertical line segment as positive infinity; 
        treat the slope of a degenerate line segment (between a point and itself) as negative infinity."""

    
    # compare two points by slopes they make with this point
    def slopeOrder(self):
        """The slopeOrder() method should return a comparator that compares its two argument points 
        by the slopes they make with the invoking point (x0, y0). 
        Formally, the point (x1, y1) is less than the point (x2, y2) if and only if the slope (y1 − y0) / (x1 − x0) 
        is less than the slope (y2 − y0) / (x2 − x0). Treat horizontal, vertical, and degenerate line segments as in the slopeTo() method."""


class Point(IPoint):

    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"({self.x},{self.y})"

    def draw(self)->None:
        plt.plot(self.x,self.y, marker="o")

    def drawTo(self, that)->None:
        x = [self.x, that.x]
        y = [self.y, that.y]
        plt.plot(x, y, marker="o")

    def compareTo(self, that)->int:
        if self.y > that.y:
            return 1
        elif self.y < that.y:
            return -1
        elif self.x > that.x:
            return 1
        elif self.x < that.x:
            return -1
        else:
            return 0

    def slopeTo(self, that)->float:
        compare = self.compareTo(that)
        # Recta vertical cuando sus "x" son iguales y "y" diferentes
        if self.x == that.x:
            # Número máximo permitido por el lenguaje 2^31-1 
            return  2**31-1
        # Recta horizontal cuando sus "y" son iguales y "x" diferentes
        elif self.y == that.y:
            return 0
        # "y" del punto actual es mayor a la posición en "y" del punto that
        elif compare == 1 : 
            slope = (self.y - that.y) / (self.x - that.x) 
        # "x" del punto actual es menor a la posición en "x" del punto that
        elif compare == -1 :
            slope = (that.y -self.y) / (that.x - self.x) 
        # Degenerate line , es decir, tienen coordenadas iguales
        else:
            # Número mínimio permitido por el lenguaje -2^31
            slope = -2**31
        return slope
    
    def slopeOrder(self):
        compare = Comparator(self)
        iterator = compare.compareSlope
        return iterator

