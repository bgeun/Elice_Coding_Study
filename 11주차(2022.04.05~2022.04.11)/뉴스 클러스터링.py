import math


def solution(str1, str2):
    answer = 0
    s1 = str1.lower()
    s2 = str2.lower()

    s1Slc, s2Slc = [], []

    for i in range(2, len(s1) + 1):
        tmp = s1[i - 2 : i]
        if tmp.isalpha():
            s1Slc.append(tmp)

    for i in range(2, len(s2) + 1):
        tmp = s2[i - 2 : i]
        if tmp.isalpha():
            s2Slc.append(tmp)
    if s1Slc == [] and s2Slc == []:
        return 65536

    s1_copy = s1Slc.copy()
    s2_copy = s2Slc.copy()

    inter = []
    for i in s1Slc:
        if i in s2_copy:
            inter.append(i)
            s1_copy.remove(i)
            s2_copy.remove(i)

    union = inter + s1_copy + s2_copy

    answer = int((len(inter) / len(union)) * 65536)

    return answer
