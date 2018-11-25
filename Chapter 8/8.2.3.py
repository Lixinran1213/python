def pet(pet_name,animal_type='dog'):
	"""没有默认值得形参要在有默认值的形参之前"""
	
	print("\nI have a "+animal_type)
	print("My "+animal_type+"'s name is "+pet_name)

pet('licco')

pet('jhjij','cat')#明确地指出了两个实参值，因此放弃使用默认值
