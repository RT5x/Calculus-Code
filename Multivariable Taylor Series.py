import math

def f(x,y,z):
  return x + math.sin(y) + z
  #Any multivariable function in the form z = f(x,y)
  
x0 = float(input("x-coordinate center: "))
y0 = float(input("y-coordinate center: "))
z0 = float(input("z-coordinate center: "))
a0 = f(x0,y0,z0)

x1 = float(input("x-coordinate of point to approximate: "))
y1 = float(input("y-coordinate of point to approximate: "))
z1 = float(input("z-coordinate of point to approximate: "))
a1 = f(x1,y1,z1)


def f_x(x,y,z):  #Partial derivative with respect to x
  h = 1e-5
  return (f(x+h, y, z)-f(x-h, y, z))/(2*h)

def f_y(x,y,z):  #Partial derivative with respect to y
  h = 1e-5
  return (f(x, y+h, z)-f(x, y-h, z))/(2*h)

def f_z(x,y,z):  #Partial derivative with respect to z
  h = 1e-6
  return (f(x, y, z+h)-f(x, y, z-h))/(2*h)
def f_xx(x,y, z):
  h=1e-7
  return (f_x(x+h, y, z) - f_x(x,y, z))/(h)
def f_yy(x,y, z):
  h = 1e-7
  return (f_y(x, y+h, z) - f_y(x,y, z))/(h)
def f_zz(x,y,z):  
  h = 1e-6
  return (f_z(x, y, z+h)-f_z(x, y, z-h))/(2*h)
def f_xy(x,y, z):
  h=1e-6
  return (f_x(x, y+h, z) - f_x(x,y, z))/(h)
def f_zx(x,y,z):  
  h = 1e-6
  return (f_z(x+h, y, z)-f_z(x-h, y, z))/(2*h)
def f_yz(x,y,z):  
  h = 1e-6
  return (f_y(x, y, z+h)-f_y(x, y, z-h))/(2*h)

dx = [f, f_x, f_xx]
dy = [f, f_y, f_yy]
dz = [f, f_z, f_zz]
dxyz = [f, f_xy, f_zx, f_yz]


ans = a0 + f_x(x0, y0, z0)*(x1 - x0) + f_y(x0, y0, z0)*(y1-y0) + f_z(x0, y0, z0)*(z1-z0) + (0.5 * f_xx(x0,y0,z0) * (x1-x0)**2) + (0.5 * f_yy(x0,y0,z0)*(y1-y0)**2) + (0.5 * f_zz(x0,y0,z0) * (z1-z0)**2) + (f_xy(x0,y0,z0)*(x1-x0)*(y1-y0)) + (f_zx(x0,y0,z0) * (z1-z0)*(x1-x0)) + (f_yz(x0,y0,z0) * (y1-y0) * (z1-z0))
print("With a center about (" + str(x0) + ", " + str(y0) + ", " + str(z0) + "), ")
print("f(" + str(x1) +", " + str(y1) + ", " + str(z1) + ") is approximately equal to : ")
print(ans)
