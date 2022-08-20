print("Given a vector function r(t) = <x(t), y(t), z(t)>, find all kinematic information.\n")
print("Edit code for x(t), y(t), and z(t) to match your function.\n")
print(" ")
t0 = float(input("Input value of t: "))

import math
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

  
r = [x(t0), y(t0), z(t0)]
v_magnitude = math.sqrt((d_x(t0))**2 + (d_y(t0))**2 + (d_z(t0))**2)
a_magnitude = math.sqrt((dd_x(t0))**2 + (dd_y(t0))**2 + (dd_z(t0))**2)


print("The velocity vector at t = " + str(t0) + " is: ")
print("<" + str(d_x(t0)) + ", " + str(d_y(t0)) + ", " + str(d_z(t0)) + ">\n")
print("The magnitude of the velocity vector at t = " + str(t0) + " is: " + str(v_magnitude) + "")

print("The acceleration vector at t = " + str(t0) + " is: ")
print("<" + str(dd_x(t0)) + ", " + str(dd_y(t0)) + ", " + str(dd_z(t0)) + ">\n")
print("The magnitude of the acceleration vector at t = " + str(t0) + " is: " + str(a_magnitude) + "")

