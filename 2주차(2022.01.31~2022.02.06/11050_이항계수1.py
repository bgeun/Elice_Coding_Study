n, k = map(int, input().split())

def factorial(num):
    if num == 1:
        return 1
    
    return num * factorial(num-1)

print(factorial(n) // (factorial(n-k) * factorial(k)))
        