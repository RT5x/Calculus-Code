import math

B = (2, 4, 3) # point you want to find the distance to
P = (1, 2, 4) # point on the line
v = (4, -2, 3) # Direction vector of the line

A = (B[0] - P[0], B[1] - P[1], B[2] - P[2])

mag_v = math.sqrt( (v[0])**2 + (v[1])**2 + (v[2])**2)
AxV = (A[1] * v[2] - A[2] * v[1],A[2] * v[0] - A[0] * v[2],A[0] * v[1] - A[1] * v[0])

mag_AxV = math.sqrt((AxV[0])**2 + (AxV[1])**2 + (AxV[2])**2)
dist = (mag_AxV)/(mag_v)

print("The distance between the line L(t) = (" + str(P[0]) + " + " + str(v[0]) + "t, " + str(P[1]) + " + " + str(v[1]) + "t, " + str(P[2]) + " + " + str(v[2]) + "t) and the point (" + str(B[0]) + ", " + str(B[1]) + ", " + str(B[2]) + ") is: \n" )
print(dist)
