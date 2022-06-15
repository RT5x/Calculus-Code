import math
from math import e

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))

print(
  """This code takes advantage of the MacLaurin approximation of e^x.
Notably, e^x = x ** n / n! as a sum for i in range(0, infty).
e = e ** 1 which is the sum of 1/n! for i in range(0, infty).
      """)

sum = 0

for i in range(0,100,1):
  sum += factorial(i) ** (-1)
  print(sum)

#Actual value of Euler's number (e):
print(math.e)
