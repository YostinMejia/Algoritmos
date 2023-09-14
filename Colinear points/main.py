from Point import *
from BruteCollinearPoints import BruteCollinearPoints
from random import randint,seed 
from FastCollinearPoints import *

def main():
    points = []
    # prueba #1
    # seed(6.499999999999993 )
    # for i in range (100):
    #     x=round(randint(0,30))
    #     y=round(randint(0,30))
    #     points.append(Point(x,y))
    
    # Prueba #2
    seed(5.799999999999995)
    for _ in range (50):
        x=round(randint(0,30))
        y=round(randint(0,30))
        points.append(Point(x,y))

    # Draw the point
    for p in points:
        p.draw() 

    colinear = BruteCollinearPoints(points)

    # colinear = FastCollinearPoints(points)
    print(points)
    print(colinear.segments())
    # Draw the lines
    for linea in colinear.segments():
        linea.draw()
    plt.show()

def buscarSeed(numLineas, numPuntos, maxX, maxY, minX=0, minY=0):
    points = [Point(0,0)]
    colinear = BruteCollinearPoints(points)
    cont =0
    while (colinear.numberOfSegments() <numLineas):
        seed(cont)
        for _ in range (numPuntos):
            x=round(randint(minX,maxX))
            y=round(randint(minY,maxY))
            points.append(Point(x,y))
        try:
            colinear = BruteCollinearPoints(points)
        except:
            pass
        cont+=0.1
        points=[]
    return cont


if __name__=="__main__":
    main()
