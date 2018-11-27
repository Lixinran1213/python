"""使用为完成练习 7-8 而创建的列表sandwich_orders，并确保'pastrami'在其中至少出现了三次
在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；
再使用一个 while 循环将列表 sandwich_orders 中的'pastrami'都删除。
确认最终的列表 finished_sandwiches 中不包含'past"""

sandwich_type = ['S1','pastrami','S3','pastrami','S4','pastrami']
finished_sandwiches = []
print('熟食店的五香烟熏牛肉卖完了\n')
while 'pastrami' in sandwich_type:
	sandwich_type.remove('pastrami')
print(sandwich_type)

act = True
while act:
	if int(len(sandwich_type)) != 0:
		sad = sandwich_type.pop()
		finished_sandwiches.insert(0,sad)
	else:
		act = False
print('\n这个是finished_sandwiches列表')
print(finished_sandwiches)
