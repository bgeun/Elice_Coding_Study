from itertools import permutations


def isprime(num):
    if num == 1 or num == 0:
        return False
    else:
        for i in range(2, int(num ** (1 / 2) + 1)):
            if num % i == 0:
                return False
    return True


def solution(numbers):
    answer = 0
    num_lst = list(numbers)

    lst_com = []

    for i in range(1, len(numbers) + 1):
        tmp = permutations(num_lst, i)
        lst_com.extend(tmp)

    lst_com = list(set(map(int, map("".join, lst_com))))

    # print(lst_com)

    for i in lst_com:
        if isprime(i):
            answer += 1

    return answer
