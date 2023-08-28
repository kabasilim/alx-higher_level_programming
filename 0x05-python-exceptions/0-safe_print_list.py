#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	count = 1
	while (count <= x):
	try:
		print("{}".format(my_list[count -1]), end="")
		count += 1
	except Exception as error:
		break
	print("")
	return count - 1
