input = 2
prime_number = list()

def prime_check(num):
    i = 2

    while num >= i:
        if num%i==0:
            break
        i += 1
    
    if num==i:
        prime_number.append(num)
        

while len(prime_number) < 10001:
    prime_check(input)
    input+=1

for i in range(len(prime_number)):
    print(prime_number[i])