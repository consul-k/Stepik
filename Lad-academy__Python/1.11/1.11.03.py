def is_year_leap(x):
	if x%4 == 0:
		if x%400 == 0:
			print('True')
		elif x%100 != 0:
			print('True')
		else:
			print('False')
	else:
		print('False') 
			
is_year_leap(int(input()))
