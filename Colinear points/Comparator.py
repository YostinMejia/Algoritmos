
class Comparator:

    def __init__(self, invokingPoint) -> None:
        self.invokingPoint = invokingPoint

    def compareSlope(self, point1, point2 ):
        
        compareSlope1 = self.invokingPoint.slopeTo(point1)
        compareSlope2 = self.invokingPoint.slopeTo(point2)
        
        if compareSlope1 > compareSlope2:
            return 1
        elif compareSlope1 < compareSlope2:
            return -1
        # Colineales
        else:
            return 0