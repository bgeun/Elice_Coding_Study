def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        k = ""
        tmp = bin(arr1[i] | arr2[i])[2:]
        tmp = "0" * (n - len(tmp)) + tmp
        for i in tmp:
            if i == "1":
                k += "#"
            elif i == "0":
                k += " "

        answer.append(k)

    return answer
