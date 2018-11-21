love = ['taylor swift','the great wall','yellow river','vienna','north pole','chinese'] # 列表①

print(love)   #打印列表

print("\nMy favorite singing star is "+love[0].title()+"\n")   #访问列表里的索引为0的元素

print(love[-1].title()+" is the language of china. \n")  #访问列表里的索引为-1的元素

love[2] = "the Yangtse River"  #修改列表里索引为2的元素  ②
print(love)

love.append('Steam Pot Chicken')  #在列表②末尾添加元素   ③
print(love)

love.insert(4,'gun') #在列表③索引为4的元素前，加入一个元素，原来索引为4的元素现在的索引为5  ④
print(love)

del love[2]    #删除④列表里索引为2的元素，不保留值  ⑤
print(love)  

love.pop()     #删除⑤列表里最后一个元素，保留其值  ⑥
print(love)

love.pop(1)    #删除⑥列表里索引为1的元素，保留其值  ⑦
print(love)

love.remove('gun')   #删除⑦列表里值为 gun 的元素，其值继续可用  ⑦
print(love)

love.sort()    #按字母先后顺序来排列⑦列表里的元素，如果列表里有大写和小写，则会出现没有按字母顺序来排列的错误  ⑧
print(love)

love.sort(reverse=True)    #按字母先后顺序的反向顺序来排列⑧列表里的元素 ⑨
print(love)

print(sorted(love))   #按字母先后顺序来排列⑨列表里的元素（暂时性的）⑩
print(love)      #和⑨列表里的的排列顺序一致  ⑪

print(sorted(love,reverse=True))   #按字母先后顺序的反向顺序来排列⑪列表里的元素（暂时性的）⑫
print(love)      #和⑨列表里的的排列顺序一致  ⑬

love.reverse()   #把⑬列表里的元素反过来排序打印 ⑭
print(love)

love.reverse()   #把⑭列表里的元素反过来排序打印，合和⑬和⑨的排列顺序一致 ⑮
print(love)

print(len(love))  # 统计列表⑮里有几个元素
