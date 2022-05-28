
def func(the_list):
	new_string = ""
	for element in the_list[0:-1]:
		new_string += element + ',' + ' '
	new_string += "and " + the_list[-1]
	return new_string

test_list = ['spam', 'bananas', 'tofu', 'apples']
answer = func(test_list)
print(answer)