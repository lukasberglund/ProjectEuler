import math
mileage_dict = {1: 0, 2: 0, 145: 0, 169: 2, 1454 : 2, 363601: 2, 871 : 1, 45361: 1, 872: 1, 45362: 1}
def get_one_digit_facts():
    one_digit_facts = {}
    for i in range(10):
        one_digit_facts[i] = math.factorial(i)
    return one_digit_facts
one_digit_facts = get_one_digit_facts()

def test():
    print(get_mileage(69))
    # print(get_mileage())
    print(dig_fact(363600))

def main():
    a = 0
    for i in range(1000000):
        # print(i)
        if get_mileage(i) == 60:
            # print('hey')
            a += 1
    print(a)


def get_mileage(n):
    if n in mileage_dict.keys():
        return mileage_dict[n]
    else:
        # prev_numbs = []
        counter = 1
        m = n
        while True:
            m_new = dig_fact(m)
            if m == m_new:
                mileage_dict[n] = counter - 1
                return counter
            m = m_new
            counter += 1
            if m in mileage_dict.keys():
                mileage_dict[n] = counter + mileage_dict[m] - 1
                return counter + mileage_dict[m]

def dig_fact(n):
    if n == 0:
        return 1
    else:
        result = 0
        while n > 0:
            result += one_digit_facts[n % 10]
            n = n // 10
        return result





main()
# test()
