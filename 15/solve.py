from time import sleep
"""
how_many = {"0,0" : 0}

def how_many_solutions(x, y):
	coordstr = str(x) + ':' + str(y)
	if coordstr in how_many:
		return how_many[coordstr]
	elif x * y == 0:
		return 1
	else:
		n = how_many_solutions(x - 1, y) + how_many_solutions(x, y - 1)
		how_many[coordstr] = n
		return n

print(how_many_solutions(3, 3))
"""
while True:
	n = input("""What's your name \n""")
	if n[0] == 'f':
		print('you are awesome')
	else:
		print('you are alright')
	print('\n')
	sleep(1)
