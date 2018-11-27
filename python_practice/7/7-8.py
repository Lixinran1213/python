"""创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名字；
再创建一个名为 finished_sandwiches 的空列表。
遍历列表 sandwich_orders，对于其中的每种三明治，都打印一条消息，
如 I made your tuna sandwich，并将其移到列表finished_sandwiches。
所有三明治都制作好后，打印一条消息"""

sandwich_type = ['鸡肉三明治','兔肉三明治','番茄三明治','起司三明治']
finished_sandwiches = []
act = True
while act:
	if int(len(sandwich_type)) != 0:
		sad = sandwich_type.pop()
		print("我给你做了"+sad)
		finished_sandwiches.insert(0,sad)
	else:
		act = False
print("\n这些三明治都做好啦:")
print(finished_sandwiches)

