def f(x):
  return x**2 
a = float(input("Starting x value: "))
b = float(input("Final x value: "))
n = float(input("Number of subintervals: "))
dx = (b-a) / n
f1 = f(a)
f2 = f(b)

sum = 0
i = 1
while i <= n:
  sum += f(a + i * dx) * dx
  i+=1

print("f(x) integrated from x = " + str(a) + " to x = " + str(b) + " is: ")
print(sum)
