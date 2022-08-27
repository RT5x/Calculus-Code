import math

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def f(x):
  return math.sin(x)
    #input function you want to approximate here

c = float(input("Taylor series centered around c = : "))
m = int(input("Order of the Taylor approximation: "))
z = float(input("This Taylor series will approximate f(x) at x = : "))

def f_x(x):
  h = 1e-6
  return (((f(x+h) - f(x)))/ h)
def f_xx(x):
  h = 1e-6
  return (((f_x(x+h) - f_x(x)))/ h)
def f_xxx(x):
  h = 1e-6
  return (((f_xx(x+h) - f_xx(x)))/ h)
def f_xxxx(x):
  h = 1e-6
  return (((f_xxx(x+h) - f_xxx(x)))/ h)
def f_xxxxx(x):
  h = 1e-6
  return (((f_xxxx(x+h) - f_xxxx(x)))/ h)

d = [f(c), f_x(c), f_xx(c), f_xxx(c), f_xxxx(c), f_xxxxx(c)]
sum = 0
i=0
while(i <= m):
  sum += (d[i] * ((z - c) ** i)) / (factorial(i))
  i = i + 1
  

print("The value f(" + str(z) + ") approximated using a Taylor series centered about c = " + str(c) + " is: ")
print(sum)
