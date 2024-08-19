import numpy as np
import Mesh as mesh
import Point as point
import matplotlib.pyplot as plt

def readCords(filepath):
    
    with open(filepath, "r") as file:
        xs, ys = file.readlines()
        xs = [float(num) for num in xs.split()]
        ys = [float(num) for num in ys.split()]

        return [xs, ys]
    

def readElem(filepath):
    elems = []
    
    with open(filepath, "r") as file:
        xs, ys, zs= file.readlines()
        xs = [float(num) for num in xs.split()]
        ys = [float(num) for num in ys.split()]
        zs = [float(num) for num in zs.split()]

    for i in range(len(xs)):
        elems.append([int(xs[i]), int(ys[i]), int(zs[i])])

    return elems


def function(p):
    return 1

if __name__ == "__main__":
    cords = readCords("./meshes/coordinates_dolfin_coarse.txt")
    elem = readElem("./meshes/nodes_dolfin_coarse.txt")
    
    mesh = mesh.Mesh(cords, elem)

    area = mesh.area()

    integral = mesh.integral(function)

    print("Total area is ", area)
    print("The integral of the function over the area is ", integral)
    print("Difference ", area-integral)

   
    mesh.draw()
    

    