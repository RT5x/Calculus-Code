import math

#Line 1:
B = (2, 4, 3) # point on line 2
u = (2, 4, -2) # Direction vector of line 2

#Line 2:
P = (1, 2, 4) # point on  line 1
v = (4, -2, 3) # Direction vector of  line 1

PB = (P[0] - B[0], P[1] - B[1], P[2] - B[2])
n = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
mag_n = math.sqrt((n[0])**2 + (n[1])**2 + (n[2])**2)

dot = (PB[0]*n[0]) + (PB[1]*n[1]) + (PB[2]*n[2])
dist = dot/mag_n
print("The distance between the line L(t) = (" + str(P[0]) + " + " + str(v[0]) + "t, " + str(P[1]) + " + " + str(v[1]) + "t, " + str(P[2]) + " + " + str(v[2]) + "t) and the line s(t) = (" + str(B[0]) + " + " + str(u[0]) + "t, " + str(B[1]) + " + " + str(u[1]) + "t, " + str(B[2]) + " + " + str(u[2]) + "t) is: \n")

print(dist)
