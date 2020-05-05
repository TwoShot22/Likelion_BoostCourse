answer = 0
sum = 0

for a in range(100):
    for b in range(100):
        for c in str(a**b):
            sum += int(c)

        if(answer<sum):
            answer=sum
        sum=0

print(answer)