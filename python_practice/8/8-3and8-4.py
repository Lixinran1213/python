#8-3
"""编写一个名为 make_shirt()的函数，它接受一个尺码以及要印到 T 恤上
的字样。这个函数应打印一个句子，概要地说明 T 恤的尺码和字样"""
def make_shirt(size,model):
	print('The size of this shirt is '+str(size)
	+' and the modle is '+model)
make_shirt(34,'"I love china"')	

print('\n————————————————————————分界线———————————————————————————\n')

#8-4
"""修改函数 make_shirt()使其在默认情况下制作一件印有字样“I love Python”的大号T恤
调用这个函数来制作如下T恤：一件印有默认字样的大号T恤
一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）"""
def make_shirt(size,model='"I love china"'):
	print('The size of this shirt is '+(size)
	+' and the modle is '+model)
make_shirt('L')
make_shirt('M','"I love Python"')
