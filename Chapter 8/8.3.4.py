def get_name(first_name,last_name):
	full_name = first_name + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter'q' at any time to quit))")
	f_name = input("First name:")
	if f_name == 'q':#给用户提供退出程序的方式
		break
	l_name = input("Last name:")
	if l_name == 'q':
		break
	while_name = get_name(f_name,l_name)
	print("\nHello, "+while_name)
