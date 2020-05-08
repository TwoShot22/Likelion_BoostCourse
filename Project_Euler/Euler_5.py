import math

answer = 1
for i in range(1, 21):
	answer *= i // math.gcd(i, answer)
print(answer)

# num = 20

# def ifDividesAll(num):
#     for i in range(2,21):
#         print(i)
#         if num%i !=0:
#             return False
#     return True

# while True:
#     if ifDividesAll(num):
#         break
#     else:
#         num+=1
# print(num)