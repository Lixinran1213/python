pizza = ['fruit pizza','seafood pizza','Rural pizza']
friend_pizza = pizza[:]
pizza.append('vagetable pizza')
friend_pizza.append('chick pizza')
for mypizza in pizza:
	print("My favorite pizza is "+mypizza+"\n")
for frinedpizza in friend_pizza:
	print("My friend favorite pizza is "+frinedpizza+"\n")
