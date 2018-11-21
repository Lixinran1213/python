plays = ['allen','jack','hellen','bob','lucas',]
print(plays[0:3])

#打印任意子集
print(plays[1:4])

#不指定第一个索引
print(plays[:4])

#不指定最后一个索引
print(plays[2:])

#负数索引切片
print(plays[-3:])

print(plays)

#列表发生变化
plays.insert(-2,'shirley')
print(plays)
print(plays[-3:])
