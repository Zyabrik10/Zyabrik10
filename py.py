# ask what operator should we use
solve = str(input("Operator (+,-,/,*) "))
operetor = ("+",'-','/','*')
i = 0
# check if the operator is entered
while i < len(operetor):
# 	if it so, solve the problem
	if solve == operetor[i]:
		try:
			a      = float(input("First number: "))
			b      = float(input("Second number: "))
			result = 0
			if solve == operetor[0]:
				result += a + b
			elif solve == operetor[1]:
				result += a - b
			elif solve == operetor[2]:
				if b == 0:
					result = "cannot be divided by zero"
				else:
					result += a / b
			elif solve == operetor[3]:
				result += a * b
		except ValueError:
				result = "Error: entered 'number' is not a number" 
		print ("Answer:",result)
		break
	else:
		i += 1
else:
	print("You did not write an operator, try again")
