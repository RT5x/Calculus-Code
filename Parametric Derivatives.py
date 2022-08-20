import math
print("Goal: find dy/dx and d2y/dx2 of a parametric set of equations x(t) and y(t)" )
print(" ")
t1 = float(input("Value of t: "))
print(" ")
def x(t):
  return t**2 + 2*t - 1
def y(t):
  return math.sin(t) - t + 3*t**2
def z(t):
  return t**2 + t**3 + 2
def d_x(t):
  h = 1e-6
  return ((x(t+h) - x(t))/(h))
def d_y(t):
  h = 1e-6
  return ((y(t+h) - y(t))/(h))

def slope(t):
  return (d_y(t))/(d_x(t))

def d_slope(t):
  h = 1e-6
  return ((slope(t+h) - slope(t))/(h))
ans2 = (d_slope(t1)) / (d_x(t1))
print("dy/dx at t = " + str(t1) + " is: ")
print(slope(t1))
print(" ")

print("d2y/dx2 at t = " + str(t1) + " is: ")
print(ans2)
