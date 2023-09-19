from Point import *
from BruteCollinearPoints import BruteCollinearPoints
from random import randint,seed 
from FastCollinearPoints import *

def main():
    # error 63,78
    points = []
    # prueba #1
    seed(3.0000000000000004)
    for _ in range (80):
        x=round(randint(0,50))
        y=round(randint(0,50))
        points.append(Point(x,y))
    # Prueba #2
    # seed(5.799999999999995)
    # for _ in range (50):
    #     x=round(randint(0,30))
    #     y=round(randint(0,30))
    #     points.append(Point(x,y))

    # Draw the point
    for p in points:
        p.draw() 

    # colinear = BruteCollinearPoints(points)
    colinear = FastCollinearPoints(points)

    # (0,30)->(14,23)->
    # print(points)
    print(colinear.segments())
    print(colinear.numberOfSegments())
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
            cont+=0.2
            points=[]
            print(cont)
        
    print(points)
    
    return cont


if __name__=="__main__":
    main()

    # print(buscarSeed(40,80,50,50))
