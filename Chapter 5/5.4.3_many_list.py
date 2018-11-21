pizza = ['onion','chess','potato']
pizza_GS = ['chess','tomato','potato']
for pizza_GSs in pizza_GS:
#遍历一遍客人的列表元素，赋值到新的变量名里面
	if pizza_GSs in pizza:
#把每次的元素都和pizza列表作比较
		print('原材料已有')
	else:
		print('加入 '+pizza_GSs)
