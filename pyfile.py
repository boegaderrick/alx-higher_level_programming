#!/usr/bin/python3
primes = []
for i in range(2, 101):
	prime = True
	for j in range(2, i + 1):
		if i % j == 0 and j != i:
			prime = False
	if prime:
	 	primes.append(j)
print('Primes below 100 are: ', primes, '\n')

table = [[x * y for x in range(1, 21)] for y in range (1, 3)]
for i in table:
	for j in i:
		if j < 100:
			print(j, end='   ' if j < 10 else '  ')
		else:
			print(j, end=' ')
	print()
