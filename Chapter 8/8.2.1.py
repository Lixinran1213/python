def pet(animal_type,pet_name):
	print("\nI have a "+animal_type)
	print('My '+animal_type+"'s name is "+pet_name.title())
	
"""实参的位置顺序和形参一致"""
pet('hamster','harry')

"""多次调用函数"""
pet('dog','willie')

"""顺序很重要"""
pet('harry','hamster')
