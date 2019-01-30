cipher = open('cipher.txt').read().split('\n')[0].split(',')
cipher = [int(c) for c in cipher]
letter_frequencies = {}
print(cipher[:10])
for l in list(set(cipher)):
    frequency = len([x for x in cipher if x == l])
    letter_frequencies[l] = frequency/ len(cipher)
# print(letter_frequencies)
for k in letter_frequencies.keys():
    if letter_frequencies[k] > 0.02:
        print(str(k) + ': ' + str(letter_frequencies[k]))









highest_frequency = 0
how_frequent = {}
# for t in list(set(three_letter_combos)):
#     frequency = len([x for x in three_letter_combos if x == t])
#     how_frequent[t] = frequency
# for k in how_frequent.keys():
#     if how_frequent[k] > 2:
#         pass
#         # print(k + ': ' + str(how_frequent[k]))
# print(how_frequent)

# print(most_common)
# print(highest_frequency)
# most_common = [68, 19, 7]
# for i in range(3):
#     print(int(most_common[i]) ^ ord(['t','h','e'][i]))
#
#     possible_code = [123, 98, 48]
#     answer=''
#     for i in range(len(cipher)):
#         v = i % 3
#         answer += chr(int(cipher[i]) ^ possible_code[v])
#
#     print(answer)
print(1 ^ ord(' '))
