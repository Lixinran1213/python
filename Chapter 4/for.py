magicans = ['bob','amy','stephon']
for magican in magicans:  
#首先python先读取这行代码，得到列表里第一个元素：bob，然后把这个元素存到新变量magican里     
    print(magican)
#然后python继续读取上面的代码，输出新变量里的值，也就是bob
#此时，因为列表里还有其他值，所以python又返回到for那行代码，继续读取里边里第二个值
#然后存储到magican里面，此时的值就是amy，列表里第二个元素，然后打印出来
#循环到最后一个元素打印出来后，因为for循环后面没有代码了，程序就停止了
