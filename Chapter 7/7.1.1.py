'''
name = input('Please enter you name:\n')
print ('Hello,'+name+'!')
'''
#提示语句超过一行，创建多行字符串：
#将提示的前半部分存储在变量message里：
message = 'If you tell us who you are, we can personlize the message you see.'

#运算符+= 在变量message存储的字符串（提示的上半部分）的末尾再加上一个字符串（提示的下半部分）
message  += '\nWhat is you first name\n'

name = input(message)
print('Hello,'+name+'!')

