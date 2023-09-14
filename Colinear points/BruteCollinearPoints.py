from Exception import IllegalArgumentException
from LineSegment import LineSegment
from Point import Point
from Sort import mergeSort, binarySearch

class BruteCollinearPoints:
    def __init__(self, points:Point) -> None: #O(n^4)
        if points == None:
            raise IllegalArgumentException()        
        # Searching for repeated points
        mergeSort(points) #O(nlogn)
        for i in range(len(points)-1): #O(n)
            if binarySearch(points,points[i],i+1,len(points)) != -1: #O(nlogn)
                raise IllegalArgumentException(f"El punto {points[i]} ya está en la lista de puntos")
        
        self.lineSegments = []
        # Find all line segments containing 4 points
        for i in range (len(points)-3): #O(n)
            for j in range(i+1, len(points)-2): #O(n^2)
                for k in range(j+1,len(points)-1):  #O(n^3)
                    for l in range(k+1,len(points)): #O(n^4)
                        # Se mira si son colineales los 3 puntos, es decir, sus pendientes son iguales
                        #Luego se comparan las pendientes de dos puntos que se saben que son colineales con el ultimo punto que falta por comparar, en este caso punto "l"
                        if points[i].slopeTo(points[j]) == points[i].slopeTo(points[k]) == points[i].slopeTo(points[l]) :
                            # punto mayor y menor para trazar su linea directa y no subsegmentos
                            self.lineSegments.append(LineSegment(points[i],points[l]))

    # The number of line segments
    def numberOfSegments(self):
        return len(self.lineSegments)
    # The line segments
    def segments(self):
        return self.lineSegments