import random
randomList = []
for i in range(0,10):
	n = random.randint(1,1000)
	randomList.append(n)
	if n%2 == 0:
		print(n, 'is even')
	else:
		print(n, 'is odd')
print(randomList)	
