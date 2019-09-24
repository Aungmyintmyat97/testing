x = int(input("price: "))
if x > 150:
	print('70% off')
elif x <= 150 and x > 100:
	print('50% off')
elif x <= 100 and x > 50:
	print('20% off')
elif x <= 50:
	print('10% off')

a = float(input('Height: '))
if a > 6:
	print('very tall')
elif a <= 6 and a == 5.10 or a == 5.11:
	print('international')
elif a <= 5.9 and a > 5.6:
	print('tall')
elif a <= 5.6 and a >= 5.4:
	print('normal') 
elif a < 5.4:
	print('japu')
