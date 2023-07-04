import numpy as np
import matplotlib.pyplot as plt

## define a function that computes the n=1 st fibonnaci number, given
# the previous two fibonacci numbers 

def aliens(F, n):
     """

     Parameters
     ----------
     F : integer array
         F{n} is the n in fibonacci numbers
     n : integer
          index into F 

     Returns
     -------
     F{n+1}, at the (n+1) st Fibonacci number

     """
     
     F[n+1] = F[n]+ F[n-1]
     return F
 
F = np.zeros(100, dtype=int)
F[0] = 0
F[1] = 1

for n in range(2,99):
    F[n] = aliens(F[n-1])