class Interval():
    def __init__(self,a ,b):
        self.lb = a
        self.ub = b
    

    def value(self):
        return(self.lb, self.ub)


    def add(self, x):
        self.lb += x.lb
        self.ub += x.ub


    def sub(self, x):
        self.lb -= x.ub
        self.ub -= x.lb


    def mul(self, x):    
        self.lb = min(self.lb * x.lb, self.lb * x.ub, self.ub * x.lb, self.ub * x.ub)
        self.ub = max(self.lb * x.lb, self.lb * x.ub, self.ub * x.lb, self.ub * x.ub)


    def div(self, x):
        self.lb = min(self.lb / x.lb, self.lb / x.ub, self.ub / x.lb, self.ub / x.ub)
        self.ub = max(self.lb / x.lb, self.lb / x.ub, self.ub / x.lb, self.ub / x.ub)
    

def main():
    in1 = Interval(5,6)
    in2 = Interval(3,4)
    in1.div(in2)


    print(in1.value())



if __name__ == "__main__":
    main()