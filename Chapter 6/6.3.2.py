user = {
    'username':'ducase',
    'age':3,
    'phonenumber':13323413123,
    'sex':'woman',
    }
for v in user.keys(): 
	print('只输出键: '+v+'\n')

for v in user: #不加keys这个方法
	print('不加keys: '+v+'\n')
#只有一个新变量，默认输出键，不输出值
