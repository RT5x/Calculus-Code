import math

x = float(input("X-coordinate of point: "))
y = float(input("Y-coordinate of point: "))
z = float(input("Z-coordinate of point: "))
pointC = (x,y,z)  #Point in cartesian coordinates
print("Initial point (cartesian coordinates): " + str(pointC) + "\n")

class cartConvert():
  def convertS(x,y,z):
  # Convert to spherical
    p = math.sqrt(x**2 + y**2 + z**2)
    phi = math.acos(z/p)
    theta1 = math.acos(x / (p * math.sin(phi))) 
    #theta2 = math.asin(y / (p* math.sin(phi)))
    pointS = (p, theta1, phi)
    print("Spherical coordinates: " + str(pointS) + "\n")

  def convertC(x,y,z):
    #Convert to cylindrical
    r = math.sqrt(x**2 + y**2)
    theta3 = math.acos(x / r)
    #theta4 = math.acos(y / r)
    pointCyl = (r, theta3, z)
    print("Cylindrical Coordinates: " + str(pointCyl))


cartConvert.convertS(x,y,z)
cartConvert.convertC(x,y,z)
  
