import string
import random

def arrayGenerator(type = "int", maxSize = 0):
	arr = []
	if type=="string":
		for _ in range(maxSize):
			item = stringGenerator(random.randint(0, 20))
			arr.append(item)
	elif type=="float":
		for _ in range(maxSize):
			item = random.random() * 100
			arr.append(item)
	else:
		for _ in range(maxSize):
			item = random.randint(-100, 100)
			arr.append(item)
	return arr

def stringGenerator(size):
	str = ""
	for _ in range(size):
		str = str + random.choice(string.ascii_uppercase)
	return str