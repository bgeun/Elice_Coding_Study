def solution(nums):

    unique = len(list(set(nums)))
    length = len(nums) // 2

    if unique < length:
        return unique
    else:
        return length
