age = 19
if (age >= 16) and (age <= 33):  #加（）便于阅读，这个是两个条件，可以不加
	print('①、使用and连接两个条件')

age = 12   #只满足后面的小于等于33这个条件
if age >= 16 and age <= 33:  
	print('②、使用and连接两个条件')
#只会输出①
