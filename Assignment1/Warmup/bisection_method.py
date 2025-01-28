'''
This program includes a function which performs the bisection method to calculate a root of a polynomial within an
interval, given that there exists only one root within that interval. The function can be called by importing this
file and calling it as:
    bisection(f, a, b, tol, max_iter)
where five different input parameters are requested to call the function. They are as follows:
    f: It is a function (expression) of a single variable whose root is needed to be calculated.
    a: It is the lower limit of the interval within which the user is seeking the root.
    b: It is the upper limit of the interval within which the user is seeking the root.
    tol: It is the tolerance which dictates the accuracy of the result.
    max_iter: It defines the maximum number of iterations for which the user wants to run the code.
'''

def bisection(f, a, b, tol, max_iter):

    # Checking if the lower and upper limits are chosen properly.
    if a >= b:
        raise ValueError("a should be smaller than b.")
    if f(a)*f(b) > 0:
        raise ValueError("The values of the function at a and b should have different signs. Try changing the limits")

    if f(a) == 0:                       # Checking if lower limit itself is the solution.
        return a
    elif f(b) == 0:                     # Checking if upper limit itself is the solution.
        return b
    else:
        for i in range(max_iter):       # Actual calculation for bisection method.
            c = (a + b)/2
            if abs(f(c)) < tol or abs(b-a) < tol:
                return c
            # Updating intervals.
            if f(a)*f(c) < 0:
                b = c                   
            else:
                a = c
        # Runtime Error if the tolerance or number of iterations are unreasonable. 
        raise RuntimeError("Convergence is taking too long. Try increasing the tolerance or increasing the maximum number of iterations allowed.")