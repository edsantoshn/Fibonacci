def fibonacci(n):
	a=1
	b=1
	for i in range(n-1):
		total= a + b
		b=a
		a= total
	return b