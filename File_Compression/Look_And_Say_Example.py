now = "1"
for i in range(int(input())):
    print(now)
    now_full = ""
    now_ = ""
    check = 0
    for i in now:
        if now_ != 1:
            if check >= 1:
                now_full += str(check)
            now_ = i
            now_full += i
            check = 1
        else : 
            check += 1
    now_full += str(check)
    now = now_full
