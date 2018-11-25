example = "\nTell me something,and I will reapet it back to you."
example += "\nEnter 'quit' to end the program\n"
messag = ""
#当变量不等于quit时
while messag !='quit':
#暂停程序同时打印括号里的内容，将用户即将输入的内容存在变量messag里
	messag = input(example)
#如果用户输入的内容不是quit，打印用户输入的内容

	if messag != 'quit':

		print(messag)
#如果输入的是quit，while循环结束
	
		
