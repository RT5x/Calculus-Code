import math
from sympy import *
import numpy as np
print("Newton's Method\n")

def f(x):
    return x**2 + x
  #Any polynomial function here

def d_f(x):
    h = 1e-5
    return (f(x+h)-f(x-h))/(2*h)

#Input initial guess
x0 = float(input("Root Guess: \n"))

#Iterations needed to make approximation
k = int(input("Number of iterations (positive integer): \n"))

#Newton's method
def N(x0, k, f):
    alist = [x0]
    if k == 1:
      guess = x0 - ((f(x0))/(d_f(x0)))
      return guess
      print(guess)

    elif k < 0:
      print("Number of iterations must be a positive integer.")

    elif k%2 != 0 or (k-1)%2 !=0:
      print("Number of iterations must be a positive integer")
  
    elif k > 1 and (k%2 == 0 or (k-1)%2 ==0):
      while i < k:
        x = x0 - ((f(x0))/(d_f(x0)))
        alist.append(x)
        return x
        x1 = x0 - ((f(x))/(d_f(x)))
        return x1
        x2 = x1 - ((f(x1))/(d_f(x1)))
        return x2
        print(x2 + "\n")
        i += 1

print("Root Approximation: ")
print(round(N(x0, k, f), 4))
