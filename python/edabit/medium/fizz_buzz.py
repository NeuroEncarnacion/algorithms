# Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

# 1. If the number is a multiple of 3 the output should be "Fizz".
# 2. If the number given is a multiple of 5, the output should be "Buzz".
# 3. If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# 4. If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
# 5. The output should always be a string even if it is not a multiple of 3 or 5.

# Examples:
# fizz_buzz(3) ➞ "Fizz"

# fizz_buzz(5) ➞ "Buzz"

# fizz_buzz(15) ➞ "FizzBuzz"

# fizz_buzz(4) ➞ "4"

# Notes:
# Try to be precise with how you spell things and where you put the capital letters.


def fizz_buzz(num):
	if num % 3 == 0 and num % 5 == 0:
		return "FizzBuzz"
	elif num % 3 == 0:
		return "Fizz"
	elif num % 5 == 0:
		return "Buzz"
	else: 
		return str(num)


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(4))