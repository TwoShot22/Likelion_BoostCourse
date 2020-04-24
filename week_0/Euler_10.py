input = 2000000
prime_number = []

# 에라토스테라스의 체

a = [False, False] + [True]*(input-1)

for i in range(2, input+1):
    if a[i]:
        prime_number.append(i)
        for j in range(2*i, input+1, i):
            a[j] = False

print(sum(prime_number))