n, m = map(int, input().split())


def get_gcd(a, b):
    while(b != 0):
        tmp = a % b

        a, b = b, tmp
    return a


gcd = get_gcd(n, m)
lcm = int(n * m / gcd)

print(gcd)
print(lcm)
