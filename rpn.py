#!/usr/bin/env python3

def addNums(arg1, arg2):
	return arg1 + arg2

operators = {
	'+': addNums
}

def calculate(arg):
	stack = list()
	for val in arg.split():
		try:
			num = int(val)
			stack.append(num)
		except ValueError:
			operation = operators[val]
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = operation(arg1, arg2)
			stack.append(result)
		print(stack)
	if len(stack) != 1:
		raise TypeError("Incorrect number of parameters")
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> '))
		print('Result: ', result)

if __name__ == '__main__':
	main()
