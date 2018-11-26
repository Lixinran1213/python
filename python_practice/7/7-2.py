message = "wellcome to reserve the seats "
message += "We want to know how many people need seats?\n"

number = input(message)
number = int(number)

if number > 8:
	print("Sorry,we don't have such big table")
else:
	print("OK,you are already reserved "+str(number)+" reserves!")
