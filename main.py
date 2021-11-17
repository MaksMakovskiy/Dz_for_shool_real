from over_school.first import zadacha_1
from over_school.third import zadacha_3
from over_school.fourth import zadacha_4
from over_school.fifth import zadacha_5
from over_school.sixth import zadacha_6
from over_school.seventh import zadacha_7
from over_school.eighth import zadacha_8
def main():
	print("Выберите номер задачи(1, 3, 4, 5, 6, 7, 8)")
	settex = int(input(">>: "))
	if settex == 1:
		zadacha_1()
	elif settex == 2:
		print("Я и не нашол второй задачи")
	elif settex == 3:
		zadacha_3()
	elif settex == 4:
		zadacha_4()
	elif settex == 5:
		zadacha_5()
	elif settex == 6:
		zadacha_6()
	elif settex == 7:
		zadacha_7()
	elif settex == 8:
		zadacha_8()
	else:
		print("Выбран неправильный номер задачи")
		main()
if __name__ == "__main__":
	main()
	input(">>: ")