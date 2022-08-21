  #vector field of components P, Q, R
def P(x,y,z): 
    return x**2 * y - y**3 + x*y + z 
def Q(x,y,z): 
    return y**2
def R(x,y,z): 
    return z**2 + x**2


def P_x(x,y,z):
  h = 1e-5
  return ((P(x+h, y,z) - P(x,y,z))/(h))
def Q_y(x,y,z):
  h = 1e-5
  return ((Q(x, y+h,z) - Q(x,y,z))/(h))
def R_z(x,y,z):
  h = 1e-5
  return ((R(x, y,z+h) - R(x,y,z))/(h))

x0 = float(input("x-coordinate of the point where divergence is calculated: "))
y0 = float(input("y-coordinate of the point where divergence is calculated: "))
z0 = float(input("z-coordinate of the point where divergence is calculated: "))

x1 = P_x(x0, y0, z0)
y1 = Q_y(x0, y0, z0)
z1 = R_z(x0, y0, z0)

print("Divergence of F = Pi + Qj + Rk at the point (" + str(x0) + ", " + str(y0) + ", " + str(z0) + "): ")
print(round(x1 + y1 + z1, 4))
