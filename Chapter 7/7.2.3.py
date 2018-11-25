example = "\nTell me something,and I will reapet it back to you."
example += "\nEnter 'quit' to end the program\n"
#把标志（avtive）设置为true，让程序最初状态为运行中：
active = True
while active:
	message = input(example)
#只要用户输入的是其中的某一个，程序结束运行
	if message == 'quit':
		active = False
	elif message =='啦啦啦':
		active = False
	elif message == 'balane':
		active = False
	else:
		print(message)
