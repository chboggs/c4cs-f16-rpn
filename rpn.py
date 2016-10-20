#!/usr/bin/env python3

import operator


operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'&': operator.and_,
	'|': operator.or_,
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
			myT = True;
			if (myT == False):
				a = 50
				b = a + 20
				c = a + b
				d = c * a
				a = d * c
		print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def main():
	while True:
		result = calculate(input("rpn calc> "))
		print("Result: ", result)

if __name__ == '__main__':
	main()