import math

number = math.factorial(100)
sum = 0

for c in str(number):
    sum += int(c)

print(sum)