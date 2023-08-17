""" examines 4 points at a time and checks whether they all lie on the same line segment, returning all such line segments. 
To check whether the 4 points p, q, r, and s are collinear, check whether the three slopes between p and q,
 between p and r, and between p and s are all equal."""
from Exception import IllegalArgumentException
from Point import Point
from LineSegment import LineSegment
class BruteCollinearPoints:
    # Find all line segments containing 4 points
    def __init__(self, points:Point) -> None:
        if points == None:
            raise IllegalArgumentException()
        self.points = points
        self.numberSegments = 0 
        self.lineSegments = []
        N = len(points)

        for i in range (N):
           
            for j in range(i+1, N):
                         
                for k in range(j+1,N):
                         
                    for l in range(k+1,N):
                        # Se mira si son colineales los 3 puntos, es decir, sus pendientes son iguales
                        #Luego se comparan las pendientes de dos puntos que se saben que son colineales con el ultimo punto que falta por comparar, en este caso punto "l"
                        if self.points[i].slopeTo(self.points[j]) == self.points[i].slopeTo(self.points[k]) == self.points[i].slopeTo(self.points[l]) :
                            # punto mayor y menor para trazar su linea directa y no subsegmentos
                            self.lineSegments.append([self.points[i],self.points[j],self.points[k],self.points[l]])
                            self.numberSegments +=1
                        # Puedo tener los puntos colineales , luego hacer un merge para ordernarlos y trazar la recta desde el mayor al menot

       
    # The number of line segments
    def numberOfSegments(self):
        return self.numberSegments
    # The line segments
    def segments(self):
        pass

a = Point(2,3)
b = Point(1,3)
c = Point(7,3)
d = Point(3,3)
list = [a,b,c,d]

x = BruteCollinearPoints(list)
print(x.points)
print(x.lineSegments)
# print(x.points)
