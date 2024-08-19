import numpy as np
import math
import matplotlib.pyplot as plt
import Point as point
import random

class Mesh():

    def __init__(self, *args):
        self.mesh = (args[0], args[1])
        self.determinants = self.__CalcDeterminants__()

    def draw(self):
        cords, elements = self.mesh
        plt.figure()

        for elem in elements:
            e1, e2, e3 = elem

            p1 = point.Point(cords[0][e1 -1], cords[1][e1 -1])
            p2 = point.Point(cords[0][e2 -1], cords[1][e2 -1])
            p3 = point.Point(cords[0][e3 -1], cords[1][e3 -1])
            
            plt.fill([p1.x, p2.x, p3.x, p1.x], [p1.y, p2.y, p3.y, p1.y])
            plt.plot([p1.x, p2.x, p3.x, p1.x], [p1.y, p2.y, p3.y, p1.y], color="white")
            
        plt.show()    


    # Concept and proof of formula:
    # https://www.cuemath.com/geometry/area-of-triangle-in-coordinate-geometry/
    def area(self):
        totalArea = 0
        cords, elements = self.mesh

        for elem in elements:
            e1, e2, e3 = elem

            p1 = point.Point(cords[0][e1 -1], cords[1][e1 -1])
            p2 = point.Point(cords[0][e2 -1], cords[1][e2 -1])
            p3 = point.Point(cords[0][e3 -1], cords[1][e3 -1])

            area = 0.5 * abs(p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y))
            #area = 0.5 * abs(mesh.determinants[n])

            totalArea += area

        return totalArea
    

    def integral(self, fun):
        partialIntegrals = []
        cords, elements = self.mesh

        for n, elem in enumerate(elements):
            e1, e2, e3 = elem

            p1 = point.Point(cords[0][e1 -1], cords[1][e1 -1])
            p2 = point.Point(cords[0][e2 -1], cords[1][e2 -1])
            p3 = point.Point(cords[0][e3 -1], cords[1][e3 -1])

            I_unit = 1/6 * (fun(p1)+fun(p2)+fun(p3)) * abs(self.determinants[n])

            partialIntegrals.append(I_unit)


        return sum(partialIntegrals)

    def __CalcDeterminants__(self):
        determinants = []
        for elem in self.mesh[1]:
            if self.__minAngle__(elem) <= 0:
                raise ValueError("To small of an angle")
            determinants.append(self.__determinant__(elem))
        
        return determinants
            

    def __minAngle__(self, element):
        cords, elem = self.mesh
        
        e1, e2, e3 = element

        p1 = point.Point(cords[0][e1 -1], cords[1][e1 -1])
        p2 = point.Point(cords[0][e2 -1], cords[1][e2 -1])
        p3 = point.Point(cords[0][e3 -1], cords[1][e3 -1])

        a = self.__sideLength__(p1, p2)
        b = self.__sideLength__(p2, p3)
        c = self.__sideLength__(p3, p1)

        A = self.__calcAngle__(a, b, c)
        B = self.__calcAngle__(b, a, c)
        C = self.__calcAngle__(c, a, b)
   
        return min(A,B,C)

    def __jacobian__(self, element):
        cords, elem = self.mesh
        
        e1, e2, e3 = element

        n11 = cords[0][e2-1] - cords[0][e1-1]
        n12 = cords[0][e3-1] - cords[0][e1-1]
    
        n21 = cords[1][e2-1] - cords[1][e1-1]
        n22 = cords[1][e3-1] - cords[1][e1-1]

        return [[n11,n12], [n21, n22]]

        

    def __determinant__(self, element):

        J = self.__jacobian__(element)

        return J[0][0] * J[1][1] - J[0][1] * J[1][0]
    


    def __calcAngle__(self, a, b, c):
        return math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    

    def __sideLength__(self, p1, p2):
        return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

