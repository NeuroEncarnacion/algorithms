# Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.

#Examples :
#factorial(3) ➞ 6

#factorial(5) ➞ 120

#factorial(13) ➞ 6227020800

#Notes:
#Assume all inputs are greater than or equal to 0.


def factorial(num):
	result = 1
	for i in range(1, num+1):
		result = result * i
	return result

print(factorial(3)) # 6
print(factorial(5)) # 120
print(factorial(13)) # 6227020800