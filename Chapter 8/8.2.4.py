def pet(pet_name,animal_type='dog'):
	print("\nI have a "+animal_type)
	print("My "+animal_type+"'s name is "+pet_name)
pet('will')   #位置实参+默认值
pet(pet_name='wille')   #位置实参+默认值
pet('hallr','hamster')  #位置实参
pet(pet_name='lily',animal_type='cat')#关键字实参
pet(animal_type='cat',pet_name='lily')#关键字实参，可换位置
