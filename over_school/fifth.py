def zadacha_5():
	a = int(input("Введите первое число: "))
	b = int(input("Введите второе число: "))
	c = 0
	if a >= b:
		print("Первое число не может быть больше второго, или иметь такоеже значение!")
		zadacha_5()
	else:
		for i in range(a, b+1):
			c+=i
	print(c)
if __name__ == "__main__":
	zadacha_5()