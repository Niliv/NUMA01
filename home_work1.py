import numpy as np
import argparse
import matplotlib.pyplot as plt

# Task1 
# Function that approximates the value of ln(x) in n number of steps.
def approx_ln(x, n):
    # Initiliaze a0 and g0
    a_i = (1+x)/2        
    g_i = np.sqrt(x)     

    # Update values for each step
    for i in range(n):
        a_next = (a_i+g_i)/2
        g_next = np.sqrt(a_next*g_i)

        a_i = a_next
        g_i = g_next

    # Calculate approximation
    approx = (x-1)/a_i

    return approx


# Task 4
def fast_approx_ln(x, n):
    # Initiliaze a0 and g0
    a_i = (1+x)/2        
    g_i = np.sqrt(x)
    
    # Initiliaze d matrix
    d = np.zeros((n+1, n+1)) 


    for i in range(n+1):
        d[0][i] = a_i
        
        # Calcualte d
        for k in range(1,i+1):
            d[k][i] = (d[k-1][i] - 4**(-k) * d[k-1][i-1])/ (1 - 4**(-k))

        
        # Update a and g
        a_next = (a_i+g_i)/2
        g_next = np.sqrt(a_next*g_i)

        a_i = a_next
        g_i = g_next

    # Calculate approximation
    approx = (x-1)/d[n][n]
    
    return approx


# Task 2 & 3
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

    # Plot all figures.
    # One for the approximation and the true log value.
    # One for the difference and one for the absolute error
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


# Task 5
def scatter_plot():
    values = np.linspace(0, 20, 10000)
    
    for n in range(2,7):
        
        # Calculate the error of the fast_approx_ln function. 
        # This is done for 10 000 values between 0 and 20.
        error = [abs(fast_approx_ln(value, n) - np.log(value)) for value in values]
        
        plt.scatter(values, error, s=4, label= "iterarion" + str(n))
    
    # Plot the error behaviour
    plt.title("Error behaviour of the accelerated Carlsson method for log")
    plt.ylabel("error")
    plt.xlabel("x")
    plt.legend()
    plt.yscale('log')
    plt.ylim(10**(-19), 10**(-5))
    plt.show()
     
        
if __name__ == "__main__":
    
    # Some arguments for easier dubugging and testing
    parser = argparse.ArgumentParser(description="Values for approximation")
    parser.add_argument("--v", type=float, default=10, help="Number to approximate")
    parser.add_argument("--n", type=int, default=10, help="Number of steps")
    
    args = parser.parse_args()
    #main(args.v, args.n) #Task 1&2&3
    scatter_plot() # Task 4&5