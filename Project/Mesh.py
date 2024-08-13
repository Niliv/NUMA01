import numpy as np

class Mesh():

    def __init__(self, *args):
        self.mesh = (args[0], args[1])

    #[1, 2, 3]

    def jacobian(self, element):
        cords, elem = self.mesh
        
        e1, e2, e3 = element

        n11 = cords[0][e2-1] - cords[0][e1-1]
        n12 = cords[0][e3-1] - cords[0][e1-1]
    
        n21 = cords[1][e2-1] - cords[1][e1-1]
        n22 = cords[1][e3-1] - cords[1][e1-1]
        
        

        return [[n11,n12], [n21, n22]]

        

    def determinant(self, element):

        J = self.jacobian(element)

        return J[0][0] * J[1][1] - J[0][1] * J[1][0]
    


    def minAngle(self, element):
        cords, elem = self.mesh
        
        #[1,2,3]
        e1, e2, e3 = element
        x1 = cords[0][e1 -1]
        x2 = cords[0][e2 -1]
        x3 = cords[0][e3 -1]

        y1 = cords[1][e1 -1]
        y2 = cords[1][e2 -1]
        y3 = cords[1][e3 -1]

        # a = 1-2
        # b = 2-3
        # c = 3-1

         
        # A = cos-1(b^2+c^2-a^2 /2bc)
        # B = cos-1(a^2+c^2-b^2 /2ac)
        # C = cos-1(a^2+b^2-c^2 /2ab)




