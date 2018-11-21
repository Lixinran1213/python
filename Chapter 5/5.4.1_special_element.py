pizza_toppings = ['onion','chess','tomato']
for pizza_topping in pizza_toppings:
#特殊元素为tomato，针对该元素有另外的答案，因此采用 if-else 结构来输出
    if pizza_topping == 'tomato':
	    print("sorry we don't have tomato")
    else:
	    print("add "+pizza_topping)

print("it's your pizza！")
