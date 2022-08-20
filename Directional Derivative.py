import math

def f(x,y,z):
  return x**2 * y - x**3
  #Any multivariable function in the form z = f(x,y)

#Derivative in direction of vector u with components ux and uy
ux = float(input("x-component of the vector direction : "))
uy = float(input("y-component of the vector direction : "))
uz = float(input("z-component of the vector direction : "))
print("Directional derivative at a point: \n")
x1 = float(input("x-coordinate of the point : "))
y1 = float(input("y-coordinate of the point : "))
z1 = float(input("z-coordinate of the point : "))
#Finding magnitude of vector u

def mag_u(ux, uy, uz):
  return math.sqrt((ux)**2 + (uy)**2 + (uz)**2)

#New components of normalized vector
ux1 = ux / mag_u(ux, uy, uz)
uy1 = uy / mag_u(ux, uy, uz)
uz1 = uz / mag_u(ux, uy, uz)
#New vector u1 is now normalized

def f_x(x,y,z):  #Partial derivative with respect to x
  h = 1e-5
  return (f(x+h, y, z)-f(x-h, y, z))/(2*h)

def f_y(x,y,z):  #Partial derivative with respect to y
  h = 1e-5
  return (f(x, y+h, z)-f(x, y-h, z))/(2*h)

def f_z(x,y,z):  #Partial derivative with respect to z
  h = 1e-5
  return (f(x, y, z+h)-f(x, y, z-h))/(2*h)
  
#Two components of the gradient vector at the point (x1, y1, z1)
gradx = f_x(x1, y1, z1)
grady = f_y(x1, y1, z1)
gradz = f_z(x1, y1, z1)
ans = (gradx * ux1) + (grady * uy1) + (gradz * uz1)
print("The directional derivative at the point " + "(" + str(x1) + ", " + str(y1) + ", " + str(z1) + ") is: ")
print(str(round(ans, 3)))
