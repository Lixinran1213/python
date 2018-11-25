
def make_pizza(*toppings): 
#*表示创建一个名为toppings的空元组将所有实参封装到元组里
	print(toppings)
make_pizza('onion')
make_pizza('potato','cheese','vegetable')

#加入循环
def makes_pizza(*topings): 
	print("\nMaking a pizza with the following toppings:")
	for topping in topings:
		print("- "+topping)
makes_pizza('onion')
makes_pizza('potato','cheese','vegetable')
