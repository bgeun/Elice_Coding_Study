def solution(s):
    answer = []

    s = s[2:-2]
    lst = s.split("},{")
    lst.sort(key=lambda x: len(x))
    # print(lst)

    for i in lst:
        ii = i.split(",")
        for iii in ii:
            # print(iii)
            if iii not in answer:
                answer.append(iii)
        # print()
    answer = list(map(int, answer))
    return answer
