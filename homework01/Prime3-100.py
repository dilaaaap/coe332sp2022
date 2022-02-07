for i in range(3,100):
	for n in range(2,100):
		if i%n == 0 and n<i:
			break
		elif i%n == 0 and i == n:
			print(i)
