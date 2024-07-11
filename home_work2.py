class Interval():
    def __init__(self,a ,b):
        self.lower_bound = a
        self.uppper_bound = b
        



def main():
    in1 = Interval(5,6)
    print(in1.lower_bound)



if __name__ == "__main__":
    main()