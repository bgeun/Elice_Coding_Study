import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
end_num = 666

while(1):
    if '666' in str(end_num):
        cnt += 1
    if n == cnt:
        print(end_num)
        break
    end_num += 1
