def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    return str(int("".join(numbers)))


# 978, 97 => 97978
# 0, 0, 0 => 0
