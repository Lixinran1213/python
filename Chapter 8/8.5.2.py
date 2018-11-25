def person(first,last,**info):
#形参info前面的**让python创建一个名为info的空字典
#并将收到的所有键—值对封装到字典里
	people = {}
	people['first']=first
	people['last']=last
	for key,value in info.items():
		people[key]=value
	return people
person1 = person('alber','lin',
                 location = 'yunnan',
                 field='physic')
print(person1)
	
