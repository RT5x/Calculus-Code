import math
print("Goal: find arc length of a parametric set of equations x(t) and y(t)" )
print(" ")

a = float(input("Starting t value: "))
b = float(input("Final t value: "))
n = float(input("Number of subintervals: "))

print(" ")

#Edit x(t) and y(t) here
def x(t):
  return t**2 
def y(t):
  return t + 3*t**2

def d_x(t):
  h = 1e-6
  return ((x(t+h) - x(t))/(h))
def d_y(t):
  h = 1e-6
  return ((y(t+h) - y(t))/(h))

def f(t):
  return (math.sqrt((d_x(t))**2 + (d_y(t))**2))

dx = (b-a) / n
f1 = f(a)
f2 = f(b)
sum = 0
i = 1
while i <= n:
  sum += f(a + i * dx) * dx
  i+=1

print("x(t) and y(t) arc length from t = " + str(a) + " to t = " + str(b) + " is: ")
print(sum)
