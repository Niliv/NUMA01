class Interval():
    def __init__(self,a ,b):
        self.lb = a
        self.ub = b


    def __str__(self):
        return "[" + str(self.lb) + "," + str(self.ub) + "]"


    def __add__(self, x):
        new_lb = self.lb + x.lb
        new_ub = self.ub + x.ub
        return Interval(new_lb, new_ub)


    def __sub__(self, x):
        new_lb = self.lb - x.ub
        new_ub = self.ub - x.lb
        return Interval(new_lb, new_ub)
        

    def __mul__(self, x):    
        new_lb = min(self.lb * x.lb, self.lb * x.ub, self.ub * x.lb, self.ub * x.ub)
        new_ub = max(self.lb * x.lb, self.lb * x.ub, self.ub * x.lb, self.ub * x.ub)
        return Interval(new_lb, new_ub)


    def __truediv__(self, x):
        new_lb = min(self.lb / x.lb, self.lb / x.ub, self.ub / x.lb, self.ub / x.ub)
        new_ub = max(self.lb / x.lb, self.lb / x.ub, self.ub / x.lb, self.ub / x.ub)
        return Interval(new_lb, new_ub)
    

def main():
    in1 = Interval(1,4)
    in2 = Interval(-2,-1)
    


    print(in1 + in2)
    print(in1 - in2)
    print(in1 * in2)
    print(in1 / in2)



if __name__ == "__main__":
    main()