import numpy as np
import argparse
import matplotlib.pyplot as plt

# Task1 
# Function that approximates the value of ln(x) in n number of steps.
def approx_ln(x, n):
    # Initiliaze a0 and g0
    a_i = (1+x)/2        
    g_i = np.sqrt(x)     

    # Update values fo each step
    for i in range(n):
        a_next = (a_i+g_i)/2
        g_next = np.sqrt(a_next*g_i)

        a_i = a_next
        g_i = g_next

    # Calculate approximation
    approx = (x-1)/g_i

    return approx


def fast_approx_ln(x, n):

    a_i = (1+x)/2        
    g_i = np.sqrt(x)  

    d_i = 0
    d_k_next = 0
    for i in range(n):
        d_i = a_i
        a_next = (a_i+g_i)/2
        g_next = np.sqrt(a_next*g_i)

        a_i = a_next
        g_i = g_next

        for k in range(1, i):
            d_k_next = (d_i - 4^(-k) * d_i_prev) / (1-4^(-k))
            


    approx = 

    return approx
    


def main(value, steps):
 
    real_values = []
    approx_values = []
    dif = []

    for step in range(steps):
        log = np.log(value)
        approx = approx_ln(value, step)
        real_values.append(log)
        approx_values.append(approx)
        dif.append(approx-log)

    abs_error = [abs(num) for num in dif]

    plt.figure(1)
    plt.plot(range(steps), real_values, color='red')
    plt.plot(range(steps), approx_values, color='b')
    plt.xlabel("Number of steps")
    plt.ylabel("Value")
    plt.title("Approximation")
    plt.grid(True)

    plt.figure(2)
    plt.plot(range(steps), dif, color='g')
    plt.xlabel("Number of steps")
    plt.ylabel("Difference")
    plt.title("Difference")
    plt.grid(True)
    

    plt.figure(3)
    plt.plot(range(steps), abs_error, color='g')
    plt.xlabel("Number of steps")
    plt.ylabel("Abosolute error")
    plt.title("Absolute error")
    plt.grid(True)
    plt.show()


    
        
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Values for approximation")
    parser.add_argument("--v", type=float, default=10, help="Number to approximate")
    parser.add_argument("--n", type=int, default=10, help="Number of steps")
    
    args = parser.parse_args()
    main(args.v, args.n)