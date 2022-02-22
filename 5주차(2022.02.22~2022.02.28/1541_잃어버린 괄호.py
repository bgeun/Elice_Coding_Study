import sys

input = sys.stdin.readline

exp = input().rstrip().split("-")

sum = 0
for i in exp[0].split("+"):
    sum += int(i)

rest_exp = exp[1:]

for i in rest_exp:
    for j in i.split("+"):
        sum -= int(j)

print(sum)
