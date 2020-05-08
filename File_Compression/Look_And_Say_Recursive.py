def lookandsay(char, current_count, line):
    if current_count < line:
        i = 0
        limit = current_count
        output = ""
        while i < len(char):
            is_char_equal = char[i]
            count = 1
            
            while i+1 < len(char) and is_char_equal == char[i+1]:
                count += 1
                i += 1
            
            output += is_char_equal + str(count)
            i+=1
        print(output)

        return lookandsay(output, limit+1, line)


if __name__ == '__main__':
    line = int(input("Enter Number Of line : "))
    char = "1"
    output = lookandsay(char, 0, line)