import math

bases = [1, 2, 5, 10, 20, 50, 100, 200]

n_ways_to_make_up = {0: 1, 1: 1, 2:2}
def get_ways_to_make_up(n):
    if n in n_ways_to_make_up.keys():
        return n_ways_to_make_up[n]
    else:
        sum = 0
        for b in bases:
            if b <= n:
                sum += n_ways_to_make_up[n-b]
        if n % 2 == 0:
            sum = sum // 2
        n_ways_to_make_up[n] = sum
        return sum

def test():
    for i in range(201):
        print(get_ways_to_make_up(i))

test()
