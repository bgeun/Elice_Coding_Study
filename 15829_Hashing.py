l = int(input())
arr = list(input())

change_arr = list(map(lambda x : ord(x) - 96,arr))
sum = 0

for i in range(len(change_arr)):
    sum += change_arr[i] * pow(31,i)
    if sum > 1234567891:
        sum = sum % 1234567891

print(sum)