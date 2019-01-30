def digit_powers(n, e):
    if n == 0:
        return 0
    else:
        s = 0
        while n > 0:
            s += (n % 10) ** e
            n = n//10
        return s
def main():
    n = 2
    sum = 0
    while True:
        dp = digit_powers(n, 5)
        if dp == n:
            sum += n
            print(sum)
        elif n == 1634:
            print('fail')
        n += 1

def test():
    print(digit_powers)
main()
