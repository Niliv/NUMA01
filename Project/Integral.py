import numpy as np
import Mesh as m

def readCords(filepath):
    
    with open(filepath, "r") as file:
        xs, ys = file.readlines()
        xs = [float(num) for num in xs.split()]
        ys = [float(num) for num in ys.split()]

        return [xs, ys]
    

def readElem(filepath):
    
    with open(filepath, "r") as file:
        xs, ys, zs= file.readlines()
        xs = [float(num) for num in xs.split()]
        ys = [float(num) for num in ys.split()]
        zs = [float(num) for num in zs.split()]

        return [xs, ys, zs]



if __name__ == "__main__":
    cords = readCords("./meshes/coord1.txt")
    elem = readElem("./meshes/elementnode1.txt")
    mesh = m.Mesh(cords, elem)

    print(mesh.determinant(8))
    
    