car = ['bmw','toyota','audi','subaru']
for cars in car:        #冒号冒号！
	if cars == 'bmw':   #冒号冒号！字符需要引号
	   print(cars.upper())  #字符串里的字母全部大写	
	else:
		print(cars.title())	#字符串里的首字母大写
print("\n")
#区分大小写
for cars in car:        
	if cars == 'BMW':   #区分大小写
	   print(cars.upper())  
	else:
		print(cars.title())	
