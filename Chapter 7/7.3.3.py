information = {}
#设置一个标志，指出调查是否继续
acitive = True

while acitive:
	name = input("Please enter your name\n")
	hobby = input("What's you hobby?\n")
	
#将答案放在字典里
	information[name]= hobby
	
#看看是否有其他人参与调查
	other = input("Would you like to invite others?(yes/no)\n")
	if other == 'no':
		acitive = False #标志满足该条件就结束程序

#显示结果	
print("\n")
for name,hobby in information.items():
	print(name.title()+"'s hobby is "+hobby)
