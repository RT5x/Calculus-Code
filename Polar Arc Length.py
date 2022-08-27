import math
print("Goal: find arc length of a polar equation r(θ)" )
print("Edit r(θ) in the code to match your function. ")
print(" ")

def r(θ):  # Edit here
  return 2 - 3 * math.cos(θ)
def x(θ):
  return r(θ) * math.cos(θ)
def y(θ):
  return r(θ) * math.sin(θ)
def d_r(θ):
  h = 1e-6
  return ((r(θ + h) - r(θ))/(h))





def f(θ):
  return (math.sqrt((r(θ)) ** 2 + (d_r(θ))**2))
a = float(input("Starting θ value (radians): "))
b = float(input("Final θ value (radians): "))
n = float(input("Number of subintervals: "))
dx = (b-a) / n
f1 = f(a)
f2 = f(b)

sum = 0
i = 1
while i <= n:
  sum += f(a + i * dx) * dx
  i+=1

print("r(θ) arc length from θ = " + str(a) + " to θ = " + str(b) + " is: ")
print(sum)
