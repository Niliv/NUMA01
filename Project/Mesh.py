import numpy as np

class Mesh():

    def __init__(self, *args):
        self.mesh = (args[0], args[1])

    

    def jacobian(self, element):
        cords, elem = self.mesh
        element = (element - 1) * 3
        n11 = cords[0][element + 1] - cords[0][element]
        n12 = cords[0][element + 2] - cords[0][element]

        n21 = cords[1][element + 1] - cords[1][element]
        n22 = cords[1][element + 2] - cords[1][element]
        
        

        return [[n11,n12], [n21, n22]]

        

    def determinant(self,element):

        J = self.jacobian(element)

        return J[0][0] * J[1][1] - J[0][1] * J[1][0]
    


    



