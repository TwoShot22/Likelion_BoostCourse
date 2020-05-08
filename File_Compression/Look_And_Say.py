line = int(input("Enter Number Of line : "))
char = "1"
output = ""

for i in range(line):
    j = 0
    while j < len(char):
        # 문자열의 첫 문자부터 Count 시작
        is_char_equal = char[j]
        count = 1
        # 현재 검사중인 숫자와 다음 숫자가 동일할 때 Count를 증가시키는 조건문
        while j+1 < len(char) and is_char_equal == char[j+1]:
            count += 1
            j += 1
        # 숫자가 몇 번 Count됐는지 다음 문자열에 추가
        output += is_char_equal + str(count)
        j += 1
    # 계산된 개미 수열을 출력
    print(output)
    # 초기화
    char = output
    output = ""