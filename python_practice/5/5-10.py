current_user = ['admin','bob','amy','lavi','sunny']
new_user = ['shirley','duncan','shield','Lavi','SUnny']
for new_users in new_user:
	if new_users.lower() in [current_users.lower() for current_users in current_user]:
#使用了列表解析
		print('你的名字已被注册')
	else:
		print('注册成功')
