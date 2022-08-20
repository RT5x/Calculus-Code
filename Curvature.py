import math
print("This program finds curvature at a point for a vector function r(t) = <x(t), y(t), z(t)>.\n")
print("Edit code for x(t), y(t), and z(t) to match your function.\n")
print(" ")
t0 = float(input("Input value of t: "))
print(" ")
def x(t):
  return t**2 + 2*t
def y(t):
  return math.sin(t)
def z(t):
  return t**2 + 2
def d_x(t):
  h = 1e-6
  return ((x(t+h) - x(t))/(h))
def d_y(t):
  h = 1e-6
  return ((y(t+h) - y(t))/(h))
def d_z(t):
  h = 1e-6
  return ((z(t+h) - z(t))/(h))
def dd_x(t):
  h = 1e-6
  return ((d_x(t+h) - x(t))/(h))
def dd_y(t):
  h = 1e-6
  return ((d_y(t+h) - y(t))/(h))
def dd_z(t):
  h = 1e-6
  return ((d_z(t+h) - z(t))/(h))

r1_magnitude = math.sqrt((d_x(t0))**2 + (d_y(t0))**2 + (d_z(t0))**2)
r2_magnitude = math.sqrt((dd_x(t0))**2 + (dd_y(t0))**2 + (dd_z(t0))**2)
denominator = (r1_magnitude) ** 3

cross_i = ((d_y(t0) * dd_z(t0)) - (d_z(t0) * dd_y(t0)))
cross_j = ((d_z(t0) * dd_x(t0)) - (d_x(t0) * dd_z(t0)))
cross_k = ((d_x(t0) * dd_y(t0)) - (dd_x(t0) * d_y(t0)))
numerator = math.sqrt((cross_i)**2 + (cross_j)**2 + (cross_k)**2)
k = numerator / denominator
R = 1/k
print("The curvature at t = " + str(t0) + " is : ")
print(round(k, 4))
print(" ")
print("The radius of curvature at t = " + str(t0) + " is : ")
print(round(R, 4))
print(" ")
