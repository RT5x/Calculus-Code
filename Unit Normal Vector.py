import math
print("Unit Normal Vector Calculator")
def F(x,y,z):
  return x**2 + y**2 +z**2 - 4   #Edit F(x,y,z) here
def Fx(x,y,z):
  h = 1e-7
  return ((F(x+h,y,z) - F(x,y,z))/(h))
def Fy(x,y,z):
  h = 1e-7
  return ((F(x,y+h,z) - F(x,y,z))/(h))
def Fz(x,y,z):
  h = 1e-7
  return ((F(x,y,z+h) - F(x,y,z))/(h))

x1 = float(input("x-coordinate of the point: "))
y1 = float(input("y-coordinate of the point: "))
z1 = float(input("z-coordinate of the point: "))

mag = math.sqrt((Fx(x1,y1,z1)**2) + (Fy(x1,y1,z1)**2) + (Fz(x1,y1,z1)**2))
a = Fx(x1,y1,z1) / mag
b = Fy(x1,y1,z1) / mag
c = Fz(x1,y1,z1) / mag

print("The unit normal vector for F(x,y,z) at the point (" + str(x1) +  ", " + str(y1) + ", " + str(z1) + ") is: ")
print("<" + str(round(a, 3)) + ", " + str(round(b, 3)) + ", " + str(round(c, 3)) + ">")
