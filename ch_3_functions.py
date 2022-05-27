

def collatz(number):
	if number % 2 == 0:
		return number/2
	else:
		return 3*number + 1


# inputNum = int(input("Give me a number and I'll run the Collantz sequence on it "))
inputNum = 3

while inputNum != 1:
	answer = collatz(inputNum)
	print(answer)
	inputNum = answer
