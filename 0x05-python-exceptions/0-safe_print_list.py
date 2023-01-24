#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	m = 0
	for b in range(x):
		try:
			print("{}".format(my_list[b]), end="")
			m += 1
		except IndexError:
			break
	print("")
	return(m)
