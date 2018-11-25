'''#返回一个字典其中包含一个人的信息：
def person(first_name,last_name):
	#把值（姓和名）封装到字典中：
	person={'first':first_name,'last':last_name}
	return person#返回整个字典
	
information = person('jima','hemne')#两项信息存储在一个字典中
print(information)'''
#扩展该函数使其接受可选函数：
def person(first_name,last_name,age=''):
	person={'first':first_name,'last':last_name}
	if age:
		person['age']=age#可选函数age
	return person
information = person('jima','hemne',age=44)
print(information)
