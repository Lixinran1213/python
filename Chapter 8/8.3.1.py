def get_name(first_name,last_name):
	full_name=first_name+" "+last_name#将函数结果存储到变量full_name中
	return full_name.title()#将结果（变量full_name）返回到函数调用行
name = get_name('lilil','ladre')#调用返回值的函数并将返回的值存储到变量name里
print(name)
