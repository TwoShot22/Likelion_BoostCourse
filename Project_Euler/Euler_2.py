num1 = 1
num2 = 2
sum = 0
result = 2

while sum <= 4000000:
    sum = num1 + num2
    if sum %2 == 0:
        result += sum
    num1 = num2
    num2 = sum

print(result)