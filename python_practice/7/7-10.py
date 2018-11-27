"""编写一个程序,调查用户梦想的度假胜地,使用类似于:
“If you could visit one place in the world, where would you go?
的提示并编写一个打印调查结果的代码块"""

msg = 'If you could visit one place in the world,'
msg += 'where would you go?'
msg1 = 'Would you like to let another person respond? (yes/ no)'
location = {}
act = True
while act:
	name = input("What's your name?\n")
	place = input(msg+'\n')
	location[name] = place
	leave = input(msg1)
	if 'no' in leave:
		act = False
print('\n')
for name,place in location.items():
	print(name+" would like to visite "+place)
