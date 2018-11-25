#定义一个包含的两个形参是列表的函数
def print_modles(unprint_modles,completed_modles):
	while unprint_modles:
#循环将unprint_modles列表里的元素删除并且存将删除的元素到变量current_modles里
		current_modles = unprint_modles.pop()#直至该列表里无元素时停止while循环
		print("printing modle:"+current_modles)#打印存在变量里的元素
#将变量里的元素依次放入completed_modles列表里末尾
		completed_modles.append(current_modles)
		
#定义一个展示元素的列表，形参为已经迁移元素过来的列表
def show_completed_modles(completed_modles):
	print("\nThe following modles have been print:")
	#将列表里的元素循环打印出来：
	for completed_modle in completed_modles:
		print(completed_modle)
		
#主程序：
#给第一个函的形参（两个列表）数传入实参：
unprint_modles = ['case','robet','dgbghkx']
completed_modles = []
#调用函数
print_modles(unprint_modles,completed_modles)
show_completed_modles(completed_modles)
