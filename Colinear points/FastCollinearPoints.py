from Exception import IllegalArgumentException
from LineSegment import LineSegment
from Point import Point
from Sort import mergeSort, binarySearch

class IFastCollinearPoints:
    def __init__(self) -> None:
        """finds all line segments containing 4 or more points"""
    def numberOfSegments(self):
        """the number of line segments"""
    def segments(self):
        """the line segments"""
class FastCollinearPoints(IFastCollinearPoints): 
    def __init__(self, points:Point) -> None: 
        if points == None:
            raise IllegalArgumentException()        
        # Searching for repeated points
        mergeSort(points) #O(nlogn)
        for i in range(len(points)-1): #O(n)
            if binarySearch(points,points[i],i+1,len(points)) != -1: #O(nlogn)
                raise IllegalArgumentException(f"El punto {points[i]} ya está en la lista de puntos")
        
        # Guardar las pendientes y comparar
        slopes=[0 for _ in range(len(points))] 
        for i in range(len(points)): #O(n)   
            slopes = points.sort(key=points[i].slopeOrder())
            print(slopes)

    # The number of line segments
    def numberOfSegments(self):
        return self.numberSegments
    # The line segments
    def segments(self):
        return self.lineSegments