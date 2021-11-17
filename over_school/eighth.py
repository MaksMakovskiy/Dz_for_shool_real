def zadacha_8():
	sts = 1
	for i in range(1, 25):
		if i % 3 == 0:
			sts *= 2
			print(f"через {i} часов, амеб было: {sts}")
if __name__ == "__main__":
	zadacha_8()