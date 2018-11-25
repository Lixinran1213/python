#利用函数向列表里的每个用户发出问候
def users(names):
	for name in names:#遍历形参收到的所有元素并带入for循环体里打印
		msg = "Hello,"+name.title()
		print(msg)
		
usernames = ['lili','baobao','huano']
users(usernames)#将列表里的元素作为实参，传递给形参names
#此后再问候用户时，直接调用该函数即可
