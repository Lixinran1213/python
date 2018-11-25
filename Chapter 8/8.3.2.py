#有的人有中间名有的没有，让中间名变为可选的实参：
def get_name(first_name,last_name,middle_name=''):
#上面给可选的实参（中间名）指定一个默认值（空字符串）并将其移至形参列表末尾
#在用户不提供中间名时不使用该实参
	if middle_name :#将非空字符串不为空默解读为true
		full_name = first_name+' '+middle_name+' '+last_name
	else:
		full_name = first_name+' '+last_name
	return full_name.title()#将结果返回到函数调用行
#上面的函数体用于判断中间名（可选实参）是否为空
name = get_name('cames','laxef')#调用返回值
print(name)

name = get_name('link','oliviya','lilili')#必须确保中间名为最后一个实参
print('\n'+name)
