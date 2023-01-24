#!/usr/bin/python3
def safe_print_division(a, b):
	m = 0
	try:
		m = a / b
	except (TypeError, ZeroDivisionError):
		m = None
	finally:
		print("Inside result: {}".format(m))
		return (m)
