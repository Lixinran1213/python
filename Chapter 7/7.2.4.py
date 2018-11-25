example = "\nPlease enter the name of a city you have visited."
example += "\n(Enter 'quit' when you are finished)\n" 
while True:#while True 打头的循环将不断运行，直至遇到break语句
	city = input(example)
	if city == 'quit':
		break
	else:
		print("I'd love to go to "+city.title())
