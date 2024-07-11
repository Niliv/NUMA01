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
        return Interval(self.lb + x.lb, self.ub + x.ub)


    def __sub__(self, x):
        return Interval(self.lb - x.ub, self.ub - x.lb)
        

    def __mul__(self, x):    
        products = [self.lb * x.lb, self.lb * x.ub, self.ub * x.lb, self.ub * x.ub]
        return Interval(min(products), max(products))


    def __truediv__(self, x):

        if x.__contains__(0):
            raise ZeroDivisionError("Interval division by zero is undefined")
        
        divsions = [self.lb / x.lb, self.lb / x.ub, self.ub / x.lb, self.ub / x.ub]
        return Interval(min(divsions), max(divsions))
    

def main():
    in1 = Interval(1)
    in2 = Interval(-2,1)
    


    exit()
    print(in1 + in2)
    print(in1 - in2)
    print(in1 * in2)
    print(in1 / in2)



if __name__ == "__main__":
    main()