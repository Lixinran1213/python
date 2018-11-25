unconfirmed_user= ['alice','briand','canndace']
confirmed_user = ['yemao','dali']
#
while unconfirmed_user:
#pop（）以每次一个的方式从列表unconfirmed_user的末尾删除用户
#将被删除的用户存在user里
	user = unconfirmed_user.pop()
	print("verifying user: "+user.title())
#将被删除的用户加到列表confirmed_user里
	confirmed_user.append(user)
#循环到unconfirmed_user里没有元素，程序自动停止

#显示所有已验证的用户：
print("\nThe following users have benn confirmed:")
for confirmed_users in confirmed_user:
	print(confirmed_users.title())
