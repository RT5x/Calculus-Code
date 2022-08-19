def f(x,y):
  return (x**2)*y + (x*y) - (y**3)
  #Any function z = f(x,y) here
def f_x(x,y):  #Partial derivative with respect to x
  h = 1e-5
  return (f(x+h, y)-f(x-h, y))/(2*h)

def f_y(x,y):  #Partial derivative with respect to y
  h = 1e-5
  return (f(x, y+h)-f(x, y-h))/(2*h)

point_x = float(input("x-coordinate of the point: "))
point_y = float(input("y-coordinate of the point: "))
point_z = f(point_x, point_y)
print("z-coordinate of the point: " + str(point_z))
print("The tangent plane at the point " + "(" + str(point_x) + "," + str(point_y) + "," + str(point_z) + ") is: \n")

a = f_x(point_x, point_y)
b = f_y(point_x, point_y)
print("z = " + str(round(a, 3)) + "(x - " + str(point_x) + ") + " + str(round(b, 3)) + "(y - " + str(round(point_y, 3)) + ") + " + str(round(point_z, 3)))
