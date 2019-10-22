num = int(input('Insert a number: '))
a = [x for x in range(2, num) if num % x == 0]

def is_prime(n):
	if num > 1:
		if len(a) == 0:
			print ('Prime number')
		else:
			print ('Not prime number')
	else:
		print ('Not prime number')
	
is_prime(num)