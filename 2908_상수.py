import sys
input = sys.stdin.readline

# a, b = map(str, input().split());

# a_reverse = a[::-1];
# b_reverse = b[::-1];

# print(max(a_reverse, b_reverse));

a, b = input().split()
reversed_a = '';
reversed_b='';
for i in range(len(a)-1, -1, -1):
  reversed_a +=a[i]
for i in range(len(b)-1, -1, -1):
  reversed_b +=b[i]

print(max(int(reversed_a), int(reversed_b)))