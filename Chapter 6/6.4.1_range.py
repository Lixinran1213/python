aliens = []
for alien_number in range(30):#rang（30）的作用是告诉python重复这个循环30次
	new_alien = {'color':'blue','size':'huge','number':878}#建立的所有外星人的数据都是这个
	aliens.append(new_alien)#每个新的外星人就加在列表末尾

#使用切片来打印前5个外星人
for alien in aliens[:5]:
	print(alien)
	
#显示总共有建了几个外星人
print('\n'+str(len(aliens)))
