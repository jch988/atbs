picnic_items = {
	'apples': 5,
	'cups': 2,
	}

print(f"I am bringing {str(picnic_items.get('cups', 0))} cups")
print(f"I am bringing {str(picnic_items.get('eggs', 0))} eggs")



# use the .setdefault() method to add a dict value if it is not already there
spam = {
	'name': 'Polka',
	'age': 5,
}

# normally is would look like this
if 'color' not in spam:
	spam['color'] = 'black'
	# {'name': 'Polka', 'age': 5, 'color': 'black'}

# .setdefault() makes it simpler. One line of code
spam.setdefault('size', 'medium')
	# {'name': 'Polka', 'age': 5, 'color': 'black', 'size': 'medium'}

spam.setdefault('size', 'small')
	# {'name': 'Polka', 'age': 5, 'color': 'black', 'size': 'medium'}
	# not changed bc the key 'size' was already there



message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}
for character in message:
	count.setdefault(character, 0)					# if current character is not in dictionary, this adds it
	count[character] = count[character] + 1			# adds 1

	# {'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 
	# 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1,
	#  'p': 1, ',': 1, 'e': 5, 'k': 2}


# Use pprint module to make things look 'pretty'

import pprint
pprint.pprint(count)
	# {' ': 13,
	#  ',': 1,
	#  'A': 1,
	#  'I': 1,
	#  'a': 4,
	#  'b': 1,
	#  'c': 3,
	#  'd': 3,
	#  'e': 5,
	#  'g': 2,
	#  'h': 3,
	#  'i': 6,
	#  'k': 2,
	#  'l': 3,
	#  'n': 4,
	#  'o': 2,
	#  'p': 1,
	#  'r': 5,
	#  's': 3,
	#  't': 6,
	#  'w': 2,
	#  'y': 1}


print(pprint.pformat(count))		# same thing

