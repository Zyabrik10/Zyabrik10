solve = str(input("Оператор (+,-,/,*) "))
operetor = ("+",'-','/','*')
i = 0
while i < len(operetor):
	if solve == operetor[i]:
		try:
			a      = float(input("Певое число "))
			b      = float(input("Второе число "))
			result = 0
			if solve == operetor[0]:
				result += a + b
			elif solve == operetor[1]:
				result += a - b
			elif solve == operetor[2]:
				if b == 0:
					result = "На 0 делить нельзя"
				else:
					result += a / b
			elif solve == operetor[3]:
				result += a * b
		except ValueError:
				result = "Error: Вы ввели не число" 
		print ("ответ:",result)
		break
	else:
		i += 1
else:
	print("Вы не написали оператор, попробуйте еще раз")