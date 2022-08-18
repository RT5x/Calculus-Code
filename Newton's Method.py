import math
print("Newton's Method\n")
#Note: For greatest accuracy, choose a large number of iterations (k), and a guess (x0) close to the actual root.
def f(x):
    return x**2 + x
  #Any polynomial function here to define f(x)

def d_f(x):         #Definine f'(x)
    h = 1e-5
    return (f(x+h)-f(x-h))/(2*h)
#Input initial guess
x0 = float(input("Root Guess: "))
#Iterations needed to make approximation
k = int(input("Number of iterations (positive integer): "))
alist = [x0]
#Newton's method
def N(x0, k, f):
    if k == 1:
      guess = x0 - ((f(x0))/(d_f(x0)))
      return guess
      print(guess)
    elif k < 0:
      print("Number of iterations must be a positive integer.")
    elif k%2 != 0 or (k-1)%2 !=0:
      print("Number of iterations must be a positive integer")
    elif k > 1 and (k%2 == 0 or (k-1)%2 ==0):
      i = 0
      while i < k:  #Newton's method
        alist[i+1] = alist[i] - ((f(alist[i]))/(d_f(alist[i])))
        alist.append(alist[i+1])
        print(alist[i+1])
        i += 1
#Final answer:
print("Root Approximation: " + str(round(alist[-1])))
