import numpy as np
import matplotlib.pyplot as plt

class Interval():
    def __init__(self, *args):

        if len(args) > 1:
            self.lb = args[0]
            self.ub = args[1]
        else:
            self.lb = args[0]
            self.ub = args[0]
    

    def __str__(self):
        return "[" + str(self.lb) + "," + str(self.ub) + "]"
    
    
    def __contains__(self, r):
        return self.lb <= r < self.ub


    def __add__(self, x):
        if type(x) == Interval:
            return Interval(self.lb + x.lb, self.ub + x.ub)
        else:
            return Interval(self.lb + x, self.ub + x)


    def __radd__(self, x):
        return self.__add__(x)
    

    def __sub__(self, x):
        if type(x) == Interval:
            return Interval(self.lb - x.ub, self.ub - x.lb)
        else:
            return Interval(self.lb - x, self.ub - x)
    

    def __rsub__(self, x):
        return Interval(x - self.ub, x - self.lb)
        

    def __mul__(self, x):
        if type(x) == Interval:
            products = [self.lb * x.lb, self.lb * x.ub, self.ub * x.lb, self.ub * x.ub]
            return Interval(min(products), max(products))
        else:
            products = [self.lb * x, self.ub * x]
            return Interval(min(products), max(products))


    def __rmul__(self, x):
        return self.__mul__(x)
    

    def __truediv__(self, x):

        if x.__contains__(0):
            raise ZeroDivisionError("Interval division by zero is undefined")
        
        divsions = [self.lb / x.lb, self.lb / x.ub, self.ub / x.lb, self.ub / x.ub]
        return Interval(min(divsions), max(divsions))
    

    def __neg__(self):
        negs = [-self.lb, -self.ub]
        return Interval(min(negs), max(negs))
    

    def __pow__(self, x):
        if x % 2 == 0:
            if 0 <= self.lb:
                return Interval(self.lb**x, self.ub**x)
            if self.ub < 0:
                return Interval(self.ub**x, self.lb**x)
            else:
                return Interval(0, max(self.lb**x, self.ub**x))
        
        else:
            return Interval(self.lb**x, self.ub**x)



def task9():
    x = Interval( -2 , 2 )  # [ -2 , 2 ]
    print(x ** 2)           # [ 0 , 4 ]
    print(x ** 3)           # [ -8 , 8 ]


def task8():
    i = 1.0 + Interval(2,3)
    
    print("Addition")
    print(Interval (2 , 3 ) + 1)
    print(1 + Interval (2 , 3 ) )
    print(1.0 + Interval (2 , 3 )) 
    print(Interval (2 , 3 ) + 1.0 )

    print("Sub")
    print(1 - Interval (2 , 3 )) 
    print(Interval (2 , 3 ) - 1 )
    print(1.0 - Interval (2 , 3 )) 
    print(Interval (2 , 3 ) - 1.0 )

    print("mul")
    print(Interval (2 , 3 ) * 1 )
    print(1 * Interval (2 , 3 ) )
    print(1.0 * Interval (2 , 3 )) 
    print(Interval (2 , 3 ) * 1.0 )

    print("neg")
    print(-Interval (4 , 5 ) )

def task10():
    xl = np.linspace(0.,1,1000)
    xu = np.linspace(0.,1,1000) + 0.5
    yl = []
    yu = []

    for j in range(1000):
        i = Interval(xl[j], xu[j])
        p = 3 * i**3 - 2 * i**2 - 5 * i - 1
        yl.append(p.lb)
        yu.append(p.ub)
        


    plt.plot(xl, yl, color="blue")
    plt.plot(xl, yu, color="green")
    plt.title("p(I) = 3I^3 - 2I^2 - 5I - 1, I = Interval(x, x+0.5)")
    plt.show()



if __name__ == "__main__":
    task10()