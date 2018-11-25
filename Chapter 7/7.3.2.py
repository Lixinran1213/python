pets = ['dog','cat','goldfish','cat','rabbit','cat',1,1]
print(pets)
#循环删除cat，直到列表不在有cat
while 1 in pets:
	pets.remove(1)
#退出下循环打印一遍
print("\n")
print(pets)

