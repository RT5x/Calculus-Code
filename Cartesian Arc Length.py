import math


def f(x):
  return x**2
    #function here
def f1(x):
  h= 1e-6
  return ((f(x+h) - f(x)) / h)

def g(x):
  return math.sqrt(1 + (f1(x))**2)
  
a = float(input("Starting x value: "))
b = float(input("Final x value: "))
n = float(input("Number of subintervals: "))
dx = (b-a) / n
g1 = g(a)
g2 = g(b)

sum = 0
i = 1
while i <= n:
  sum += g(a + i * dx) * dx
  i+=1

print("f(x) arc length from x = " + str(a) + " to x = " + str(b) + " is: ")
print(sum)
