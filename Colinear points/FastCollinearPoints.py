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
            
        self.lineSegments=[]
        # Guardar las pendientes y comparar
        # En caso de ser un lenguaje fuertemente tipado Se cuentan con lista enlazada
        contColi=[]
        for i in range(0,len(points)):
            slopes = sorted(points,key=points[i].slopeTo)
            prevSlope = 0
            j=0
            while j < len(slopes):
                # Si punto[i] es mayor a slope[j] quiere decir de que los puntos ya se compararon , 
                # por lo tanto no se debería comparar ni almacenar la linea con los puntos que tengan igual pendiente del slope[j] con el punto [i]
                actualSlope = points[i].slopeTo(slopes[j])
                if points[i] < slopes[j]:# Aún no se han comparado ambos puntos
                    if actualSlope != prevSlope:
                        if len(contColi) > 3:
                            self.lineSegments.append(LineSegment(contColi[0],contColi[-1]))
                        contColi=[points[i]]
                    prevSlope = actualSlope
                    contColi.append(slopes[j])
                else: #Se compararon ambos puntos
                    if len(contColi) > 3: #Se encontró un segmento anteriormente
                        self.lineSegments.append(LineSegment(contColi[0],contColi[-1]))
                    prevSlope = actualSlope 
                    while actualSlope == prevSlope and j<len(slopes)-1: #Hasta que se encuentre un punto con difrente pendiente 
                        j+=1
                        actualSlope = points[i].slopeTo(slopes[j])
                    if j<len(slopes)-1: #Para que se compare con el punto de piendente diferente
                        j-=1
                    contColi=[points[i]] #reiniciar el segmento
                j+=1
            # Se verifica que no quede ningun segmento sin agregar
            if len(contColi) > 3:
                mergeSort(contColi)
                self.lineSegments.append(LineSegment(contColi[0],contColi[-1]))
            contColi = []
                           
    # The number of line segments
    def numberOfSegments(self):
        return len(self.lineSegments)
    # The line segments
    def segments(self):
        return self.lineSegments