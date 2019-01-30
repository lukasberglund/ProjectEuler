import math

def main():
    possibleAmicableNumbers = range(2,10001)
    amicableNumbers = [1]
    for n in possibleAmicableNumbers:
        dOfN = d(n)
        if d(dOfN) == n:
            print(n)
            amicableNumbers.append(n)
            possibleAmicableNumbers.remove(n)
            if not dOfN == n:
                amicableNumbers.append(dOfN)
                possibleAmicableNumbers.remove(dOfN)
    print(amicableNumbers)
    print(sum(amicableNumbers))

def d(n):
    return sum(divisorGenerator(n))

def divisorGenerator(n):
    yield 1
    large_divisors = []
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

main()