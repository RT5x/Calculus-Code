import math
import time
from time import sleep
# Edit x(t), y(t), z(t) and f(x,y,z) here:

def x(t):
  return t + 1
def y(t):
  return t**2 - 2*t + math.sin(t)
def z(t):
  return math.log(t) - 23*t
def f(x,y,z):
  return (x - y*x +math.sin(z**2))
  
    
a = float(input("Starting t value (a): \n"))
b = float(input("Ending t value (b): \n"))
n = int(input("Number of subintervals (n): \n"))
print(" ")
print("Calculating . . . \n")
def x1(t):
  h=1e-6
  return ((x(t+h) - x(t))/(h))
def y1(t):
  h=1e-6
  return ((y(t+h) - y(t))/(h))
def z1(t):
  h=1e-6
  return ((z(t+h) - z(t))/(h))
def g(t):
  return f(x(t), y(t), z(t)) * math.sqrt((x1(t))**2 + (y1(t))**2 + (z1(t))**2)

i = 1
sum = 0
k = 1e6
dt = (b-a)/n
while i <= n:
  sum += g(a + i * dt) * dt
  i+=1
print(" ")

print("The line integral along the function f(x,y,z) with a curve defined by r(t) = <x(t),y(t),z(t)> from t = " + str(a) + " to t = " + str(b) + " is approximately: \n")
sleep(0.5)
print(sum)
