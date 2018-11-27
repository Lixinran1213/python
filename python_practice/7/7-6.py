"""以另一种方式完成练习 7-4 或练习 7-5，在程序中采取如下所有做法：
在while循环中使用条件测试来结束循环；使用变量active来控制循环结束的时机；
用break语句在用户输入'quit'时退出循环"""
msg = ('\n请输入一种披萨配料，输入‘quit’后会退出程序，请输入：')
active1 = True
while active1:
	msgs = input(msg)
	if msgs=='quit':
		active1 = False
	else:
		print('我们会在比萨中添加这种配料: ' + msgs)

#用break语句在用户输入'quit'时退出循环
msg = "\nplease tell me your age:\n"
ac = True
while ac:
	age = input(msg)
	if 'quit' in age:
		print('已退出')
		break
	elif int(age) <3:
		print('free')
	elif 3 <= int(age) <12:
		print('10 dollars')
	elif int(age) >= 12:
		print('15 dollars')
