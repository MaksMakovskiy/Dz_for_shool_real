def zadacha_7():
	sts = 10
	for i in range(10):
		sts += sts / 100 * 10
		print(f"в {i+1} день спорцмен пробежал {round(sts, 1)}")
if __name__ == "__main__":
	zadacha_7()