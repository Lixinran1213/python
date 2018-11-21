car = ['BMW','tOYOta','dudi','SubAru']  #值的大小写不一致
for cars in car:        
	if cars.lower() == 'bmw':   #把值的字母都转换为小写，在和 bmw 作比较
	   print(cars.upper())      #依然可以输出想要的结果
	else:
		print(cars.title())	
