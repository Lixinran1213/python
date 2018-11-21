#3-4
dinner = ['mother','lover','bestfriend','grandma','grandpa']
for dinners in dinner:
	print("I would like to invite you to have dinner with me,my "+dinners.title()+".")

print("\n"+dinner[0].title()+" can't have dinner together.\n")

dinner[0]="brother"

for dinners in dinner:
	print("I would like to invite you to have dinner with me,my "+dinners.title()+".")


print("\nI found a bigger table so we can have three more guest\n")
dinner.insert(0,'husband')
dinner.insert(3,'three')
dinner.append('somebody')

for dinners in dinner:
	print("I would like to invite you to have dinner with me,my "+dinners.title()+".")

print("\nI'm so sorry,that table can't be here at time,we only have two guest to join us.\n")

#使用了两次for才删到想要的效果，再查一下
for dinners in dinner:
    dinners=dinner.pop()
    print("I am so sorry that you can't jion the dinner because of the table,my dear "+dinners.title()+".")

for dinners in dinner:
    dinners=dinner.pop()
    print("I am so sorry that you can't jion the dinner because of the table,my dear "+dinners.title()+".")

for dinners in dinner:
    print("\nYou are still in my guest list,please come to dinner at time,my "+dinners.title()+"\n")

del dinner[0]
del dinner[0]
print(dinner)
