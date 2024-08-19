import numpy as np
import Mesh as mesh
import Point as point

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


# Concept and proof of formula:
# https://www.cuemath.com/geometry/area-of-triangle-in-coordinate-geometry/
def calcArea(mesh):
    totalArea = 0
    cords, elements = mesh.mesh

    for n, elem in enumerate(elements):
        e1, e2, e3 = elem

        p1 = point.Point(cords[0][e1 -1], cords[1][e1 -1])
        p2 = point.Point(cords[0][e2 -1], cords[1][e2 -1])
        p3 = point.Point(cords[0][e3 -1], cords[1][e3 -1])

        area = 0.5 * abs(p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y))
        #area = 0.5 * abs(mesh.determinants[n])

        totalArea += area


    return totalArea

def calcIntegral(mesh, fun):
    partialIntegrals = []
    cords, elements = mesh.mesh
    
    for n, elem in enumerate(elements):
        e1, e2, e3 = elem

        p1 = point.Point(cords[0][e1 -1], cords[1][e1 -1])
        p2 = point.Point(cords[0][e2 -1], cords[1][e2 -1])
        p3 = point.Point(cords[0][e3 -1], cords[1][e3 -1])
        #print(p1,p2,p3)
        #print(fun(p1)+fun(p2)+fun(p3))
        I_unit = 1/6 * (fun(p1)+fun(p2)+fun(p3)) * abs(mesh.determinants[n])

        partialIntegrals.append(I_unit)
    

    return sum(partialIntegrals)



    


    


def function(p):
    return 1

if __name__ == "__main__":
    cords = readCords("./meshes/coord2.txt")
    elem = readElem("./meshes/elementnode2.txt")
    
    mesh = mesh.Mesh(cords, elem)

    #print(calcIntegral(mesh, function))
    #print(calcArea(mesh))

    mesh.draw()

    