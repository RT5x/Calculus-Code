import math
print("Goal: find dy/dx and d2y/dx2 of a polar equation r(θ)" )
print("Edit r(θ) in the code to match your function. ")
print(" ")
θ1 = float(input("Value of θ: "))
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
num1 = ((d_r(θ1) * math.sin(θ1)) + (r(θ1) * math.cos(θ1)))
denom1 = ((d_r(θ1) * math.cos(θ1)) - (r(θ1) * math.sin(θ1)))
ans1 = num1 / denom1
num2 = d_r(num1)
denom2 = ((math.cos(θ1) * d_r(θ1)) - (r(θ1) * math.sin(θ1)))
ans2 = num2 / denom2
print("dy/dx at θ = " + str(θ1) + " : ")
print(ans1)
print(' ')
print("d2y/dx2 at θ = " + str(θ1) + " : ")
print(ans2)
