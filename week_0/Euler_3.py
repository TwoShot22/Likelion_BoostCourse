problem = 600851475143
num = 2
answer = list()

while problem>=num:
    if problem%num==0:
        answer.append(num)
        problem /= num
    num += 1

for i in answer:
    print(i)