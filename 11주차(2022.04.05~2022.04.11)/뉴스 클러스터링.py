def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    slc1 = []
    slc2 = []

    for i in range(len(str1) - 1):
        tmp = str1[i : i + 2]
        if tmp.isalpha():
            slc1.append(tmp)
    for i in range(len(str2) - 1):
        tmp = str2[i : i + 2]
        if tmp.isalpha():
            slc2.append(tmp)
    if slc1 == [] and slc2 == []:
        return 65536

    s1_copy = slc1.copy()

    inter = []

    for i in slc1:
        if i in slc2:
            inter.append(i)
            s1_copy.remove(i)
            slc2.remove(i)

    union = inter + s1_copy + slc2

    answer = int((len(inter) / len(union)) * 65536)

    return answer
