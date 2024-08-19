import numpy as np
import math
import matplotlib.pyplot as plt
import Point as point

class Mesh():

    def __init__(self, *args):
        self.mesh = (args[0], args[1])
        self.determinants = self._CalcDeterminants()


    def draw(self):
        cords, elements = self.mesh

        radi = 0.05
        for elem in elements:
            e1, e2, e3 = elem


            p1 = point.Point(cords[0][e1 -1], cords[1][e1 -1])
            p2 = point.Point(cords[0][e2 -1], cords[1][e2 -1])
            p3 = point.Point(cords[0][e3 -1], cords[1][e3 -1])

            
            
            
        

        plt.show()


    def _CalcDeterminants(self):
        determinants = []
        for elem in self.mesh[1]:
            if self._minAngle(elem) <= 0:
                raise ValueError("To small of an angle")
            determinants.append(self._determinant(elem))
        
        return determinants
            

    def _minAngle(self, element):
        cords, elem = self.mesh
        
        e1, e2, e3 = element

        p1 = (cords[0][e1 -1], cords[1][e1 -1])
        p2 = (cords[0][e2 -1], cords[1][e2 -1])
        p3 = (cords[0][e3 -1], cords[1][e3 -1])

        a = self._sideLength(p1, p2)
        b = self._sideLength(p2, p3)
        c = self._sideLength(p3, p1)

        A = self._calcAngle(a, b, c)
        B = self._calcAngle(b, a, c)
        C = self._calcAngle(c, a, b)
   
        return min(A,B,C)

    def _jacobian(self, element):
        cords, elem = self.mesh
        
        e1, e2, e3 = element

        n11 = cords[0][e2-1] - cords[0][e1-1]
        n12 = cords[0][e3-1] - cords[0][e1-1]
    
        n21 = cords[1][e2-1] - cords[1][e1-1]
        n22 = cords[1][e3-1] - cords[1][e1-1]

        return [[n11,n12], [n21, n22]]

        

    def _determinant(self, element):

        J = self._jacobian(element)

        return J[0][0] * J[1][1] - J[0][1] * J[1][0]
    

  


    def _calcAngle(self, a, b, c):
        return math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    

    def _sideLength(self, p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

