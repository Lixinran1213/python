love = ['QWE','aaa']
for lover in love:
	if lover =='aaa':
		print('相等\n')
		
	if lover !='qwe':
		print('不等于\n')
		
	if lover.lower() =='qwe':
		print('使用lower\n')

age = 12
if age >= 5:
	print('大于等于')
if age <=20:
	print('小于等于')
if age <20:
	print('小于')
if age >1:
	print('大于\n')

sun = ['wer','sdf']
if 'wer' in sun:
	print('使用in')
if 'dfg' not in sun:
	print('使用not in\n')

pizza = ['onion','tomato','potato']
if 'onion' and 'tomato' in pizza:
	print('使用and')
if 'rrrr' or 'potato' in pizza:
	print('使用or')
