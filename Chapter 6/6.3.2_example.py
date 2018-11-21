favorite_lannguage = {
   'jema':'python',
   'sara':'c',
   'jeaf':'ruby',
   'phil':'java'
   }
friend = ['jema','jeaf']
for name in favorite_lannguage.keys():#将上面的列表里的键分别存储到新变量name里，循环打印
	print(name.title())
#下面的 if语句 判断 新变量 name 里的键是否在 friend里面，在就输出，不在就继续比较
	if name in friend:
		print(name.title()+',我知道你擅长使用'+favorite_lannguage[name].title())
