age = 12  #只满足小于33这个条件
if (age >= 16) or (age <= 33):  
	print('①、使用or连接两个条件')

age = 38   #不满足任何条件
if age <= 16 or age <= 33:  
	print('②、使用or连接两个条件')

#只会输出①

