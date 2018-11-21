#采用临时变量来创建列表

numbers = []             #创建一个空的列表
for value in range(1,11):  #把1到10的数字遍历一遍
    numberss = value**2     #新建一个临时变量，把平方后的值存进去
    numbers.append(numberss) #把临时变量的值每次都放在列表末尾
    print(numbers)         #每平方一个值就输出，然后平方1到10里的下一个数字

#不采用临时变量来创建列表
numbers = []             #创建一个空的列表
for value in range(1,11):  #把1到10的数字遍历一遍
    numbers.append(value**2) #把1到10的每一个值都平方，然后放在列表末尾
    print(numbers)       #每平方一个值就输出，然后平方1到10里的下一个数字
