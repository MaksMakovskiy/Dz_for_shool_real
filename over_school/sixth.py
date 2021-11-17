def zadacha_6():
	a = int(input("Введите первое число: "))
	b = int(input("Введите второе число: "))
	с = 0
	if a >= b:
		print("Первое число не может быть больше второго, или иметь такоеже значение!")
		zadacha_6()
	else:
		for i in range(a, b+1):
			if i % 2 == 0:
				с += i
	print(с)
if __name__ == "__main__":
	zadacha_6()
	input(">>: ")
