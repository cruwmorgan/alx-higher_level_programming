#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	m = 0
	for b in range(x):
		try:
			print("{:d}".format(my_list[b]), end="")
			m += 1
		except (ValueError, TypeError):
			b += 1
			continue
	print("")
	return (m)
