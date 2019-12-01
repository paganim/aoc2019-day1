# mass / 3 - remove 0.nn - -2

def getFuel(mass):
	mass = int(mass)
	mass /= 3
	mass = round(mass-0.4999)
	mass -= 2
	return mass

total = 0
for line in open('./pageOfCarburant'):
	total += getFuel(line)
	
print(total)
