word = input()
word = list(word.upper())

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

cnt = []
cnt.extend([0] * 26)

for i in word:
    for j in range(len(alphabet)):
        if(i == alphabet[j]):
            cnt[j] += 1
            break

max_index = cnt.index(max(cnt))

cnt.sort(reverse=True)

if(cnt[0] == cnt[1]):
    print('?')
else:
    print(alphabet[max_index])
