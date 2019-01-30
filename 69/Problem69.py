from itertools import permutations

def phi(n):
    print(n)
    print("hey")
    return len([multiplied(l) for l in allCombinations(primeFactors(n))])


def primeFactors(n):
    return [prime for prime in primes(n)
            if n % prime == 0]


def primes(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


def allCombinations(inputList):
    combinations = [inputList]
    for i in range(1, len(inputList)):
        combinations += [list(x) for x in permutations(inputList, i)]
    return combinations


def multiplied(list):
    ans = 1
    for i in list:
        ans *= i
    return ans

print(max([(long(n) / phi(long(n))) for n in range(1, 10 ** 6 + 1)]))