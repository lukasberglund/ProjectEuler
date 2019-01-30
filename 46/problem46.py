import math

def main1():
	x = 9
	while is_prime(x) or is_goldbach1(x):
		x += 2
	print(x)

def is_goldbach1(x):
	for i in range(1, math.floor(math.sqrt(x)) + 1):
		if x - 2 * i * i == 0 or is_prime(x - 2 * i * i):
			return True
	return False

def main():
	x = 9
	prime_limit = 9
	primes = get_primes_up_to(prime_limit)
	while x in primes or is_goldbach(x, primes):
		x += 2
		if prime_limit < x:
			prime_limit *= 2
			primes = get_primes_up_to(prime_limit)
	print(x)

def is_goldbach(x, primes):
	# print(x)
	print(x)
	for prime in primes:
		if x == 17:
			print(prime)
		if prime < x and is_square((x - prime) / 2):
			return True
	return False

def get_primes_up_to(x):
	n = math.ceil((x - 2) / 2)
	nums = list(range(1, n + 1))
	for m in range(1, n + 1):
		if is_def_not_prime(m):
			nums.remove(m)
	return [2] + [n * 2 + 1 for n in nums]

def is_def_not_prime(m):
	for j in range(1, math.floor((m - 1) / 3) + 1):
		for i in range(1, j + 1):
			if i + j + 2 * i * j == m:
				return True
	return False

def is_square(x):
	return math.sqrt(x) % 1 == 0

def is_prime(n):
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
  			return False
		i = i + 6
	return True

# main()
for i in range(100):
	main1()
for i in range(100):
