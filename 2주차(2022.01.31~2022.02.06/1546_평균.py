n = int(input())
arr = list(map(int, input().split()))

maxNum = max(arr)

result = (sum(arr) / maxNum) * (100/n)

print(result)