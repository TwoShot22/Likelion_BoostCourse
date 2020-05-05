TWO_DIGITS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

THREE_DIGITS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def numToEnglish(n):
	if 0 <= n < 20:
		return TWO_DIGITS[n]
	elif 20 <= n < 100:
		return THREE_DIGITS[n // 10] + (TWO_DIGITS[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return TWO_DIGITS[n // 100] + "hundred" + (("and" + numToEnglish(n % 100)) if (n % 100 != 0) else "")
	elif n == 1000:
		return "onethousand"
	else:
		print("Error")

sum = 0

for i in range(1,1001):
    sum += len(numToEnglish(i))

print(sum)