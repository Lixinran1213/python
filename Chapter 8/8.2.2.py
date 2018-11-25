def pet(animal_type,pet_name):
	print("\nI have a "+animal_type)
	print("My "+animal_type+"'s name is "+pet_name)
	
pet(animal_type='hamster',pet_name='harry')
"""可以改变顺序，但是不可以重复或者缺少参数"""
pet(pet_name='harry',animal_type='hamster')
