def main():
    answer = findAnswer([2])
    print(answer)

def findAnswer(primes):
    i = primes[-1]
    if isAnswer(i):
        return i
    else:
        return findAnswer(generateNewPrime(primes))


def isAnswer(inputInt):
    inputString = inputInt.toString


def generateNewPrime(primes):
    i = primes[-1]
    primeFound = False
    while not primeFound:
        i += 1
        if isPrime(i, primes):
            return primes + [i]

def isPrime(i, primes):
    for prime in primes:
        if i % prime == 0:
            return False
    return True
