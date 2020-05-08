sumOfSquare = 0
squareOfSum = 0

# 제곱의 합
for i in range(1,101):
    sumOfSquare += i**2

# 합의 제곱
temp = 0

for j in range(1,101):
    temp += j
squareOfSum = temp**2

print(squareOfSum - sumOfSquare)