"""The mathematician Srinivasa Ramanujan found an infinite series that can be used to
generate a numerical approximation of 1/pi. estimate_pi uses this algorithm to estimate the value of pi"""
from math import pow, sqrt, e
def factorial(n):
    """function returns the factorial of a number"""
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
        
        
 
 
def estimate_pi():
    totals=0
    estimate=0
    i=0
    while True:
        total=(factorial(4*i)*(1103+26390*i))/(pow(factorial(i), 4)*pow(396, (4*i)))
        totals=totals+total
        m=(2*sqrt(2)*totals)/9801.0
        pie=1/m
        if abs(estimate-pie)<1e-15:
            return pie
        estimate=pie
        i=i+1
        
        
print estimate_pi()
    

