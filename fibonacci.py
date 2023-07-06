import numpy as np
import matplotlib.pyplot as plt

## define a function that computes the n=1 st fibonnaci number, given
# the previous two fibonacci numbers 

def aliens(F, n):
     """

     Parameters
     ----------
     F : float array
         F{n} is the n in fibonacci numbers
     n : integer
          index into F 

     Returns
     -------
     F{n+1}, at the (n+1) st Fibonacci number

     """
     
     F[n] = F[n-1] + F[n-2]
     return F[n]
 
    
def aliens2(F, n):
    if len(F) <=2:
        print(' F is not long enough')
        return(0)
    
    """
    Parameters 
    ---------
    F : float list
        list of fibonacci numbers 
    n : integer 
    compute the n-th fibonacci number f[n]
    given F[n-1] and F[n-2]
    
    Returns 
    -------
    None.
    -------
    """
    
    F.append[F[n-1]+F[n-2]]
    return F

if __name__ == "__main__":
    
    
    ## first use an array 
    
    F = np.zeros(100)
    F[0] = 0
    F[1] = 1

    for n in range(2, 20):
        
        F[n] = aliens(F, n)
        
    intF = [int(x) for x in F[:20]]
        
    print(intF)
    ## now use a list 
    
    F = intF
    d = []
    
    for n in range(2,19):
       d.append(F[n]/F[n-1])
        
    print(d)
    
    ## to finish this, compute d[n] = F[n]/F[n-1]
    ## and for n=1 to 20 plot d[n]
 
    plt.plot(d, ".")
    plt.title("golden")
    plt.xlabel("ratio number")
    plt.ylabel("golden ratio")
    plt.grid()
    
    
    
