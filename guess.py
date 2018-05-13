import random
start = input('請決定隨機數字範圍開始值')
end = input('請決定隨機數字會為結尾值')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count = count + 1
	nub = input('請猜數字')
	nub = int(nub)
	if nub == r:
		print('終於猜對了')
		print('這是你猜的第', count, '次')
		break
	else:
		if nub > r:
			print('再猜一次，答案比較小')
		else:
			print('再猜一次，答案比較大')
	print('這是你猜的第', count, '次')
