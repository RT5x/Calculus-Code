import math
B = (2, 4, 3) # point on the line
n = (3, 0, -1)  # Normal Vector of the Plane
P = (1, 2, 4) # point on the plane
v = (3, -2, 4)  # Direction vector of the line

u = (B[0] - P[0], B[1] - P[1], B[2] - P[2])
mag_n = math.sqrt( (n[0])**2 + (n[1])**2 + (n[2])**2)

num = (u[0] * n[0]) + (u[1]*n[1]) + (u[2]*n[2])
dist = num / mag_n
print("The distance between the plane " + str(n[0]) + "(x - " + str(P[0]) + ") + " + str(n[1]) + "(y - " + str(P[1]) + ") + " + str(n[2]) + "(z - " + str(P[2]) + ") = 0 and the line L(t) = (" + str(B[0]) + " + " + str(v[0]) + "t, " + str(B[1]) + " + " + str(v[1]) + "t, " + str(B[2]) + " + " + str(v[2]) + "t) \n")
print(dist)
