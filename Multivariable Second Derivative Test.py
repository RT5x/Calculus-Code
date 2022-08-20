import math
def f(x,y):
  return x**2 + y**2
#For this test, functions f(x,y) must satisfy the mixed derivative theorem, i.e. f_xy = f_yx
def f_x(x,y):
  h=1e-7
  return (f(x+h, y) - f(x,y))/(h)
def f_y(x,y):
  h=1e-7
  return (f(x, y+h) - f(x,y))/(h)
def f_xx(x,y):
  h=1e-7
  return (f_x(x+h, y) - f_x(x,y))/(h)
def f_yy(x,y):
  h = 1e-7
  return (f_y(x, y+h) - f_y(x,y))/(h)
def f_xy(x,y):
  h=1e-7
  return (f_x(x, y+h) - f_x(x,y))/(h)
x0 = float(input("x-coordinate of critical point: "))
y0 = float(input("y-coordinate of critical point: "))
z0 = f(x0, y0)
print("z-coordinate of critical point: " + str(z0))

#if f_x(x0, y0) != 0 or f_y(x0, y0) != 0:
  #print("This is not a critical point.")
  #exit()

H = (f_xx(x0, y0) * f_yy(x0,y0)) - (f_xy(x0,y0))**2
print("H = " + str(H))
if H < 0:
  print("The point (" + str(x0) + ", " + str(y0) + ", " + str(z0) + ") is a saddle point.")
  exit()
if H == 0:
  print("The test was inconclusive.")
  exit()
if H > 0:
  print("The point (" + str(x0) + ", " + str(y0) + ", " + str(z0) + ") could be a relative maximum or minimum.")
if f_xx(x0,y0) < 0:
  print("The point (" + str(x0) + ", " + str(y0) + ", " + str(z0) + ") is a local maximum.")
if f_xx(x0,y0) > 0:
  print("The point (" + str(x0) + ", " + str(y0) + ", " + str(z0) + ") is a local minimum.")
