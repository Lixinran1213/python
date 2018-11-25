def make_pizza(size,*toppings): #加入披萨的尺寸
	print("\nMaking a "+str(size)+  #根据尺寸添加东西
	"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- "+topping)
make_pizza(67,'onion')
make_pizza(12,'potato','cheese','vegetable')
