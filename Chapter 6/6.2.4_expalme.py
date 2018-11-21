alien = {'x_alien':0,'y_alien':3,'speed':'medium'}
#这里的speed是medium，属于else里面的情况，所以向右移动了3个单位
print('原来的 X：'+str(alien['x_alien']))

#向右移动外星人
#据外星人当前速度决定将其移动多远

#修改speed的值，可以改变外星人移动的单位
alien['speed'] = 'slow'

if alien['speed'] == 'slow':
	x_increment = 1
elif alien['speed'] == 'fast':
	x_increment = 2
else:
	x_increment = 3  #这个外星人速度很快

alien['x_alien'] = alien['x_alien']+x_increment
print('新的 X：'+str(alien['x_alien']))
