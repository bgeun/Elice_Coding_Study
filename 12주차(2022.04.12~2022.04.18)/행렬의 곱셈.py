def solution(arr1, arr2):
    answer = []
    x = len(arr2[0])
    y = len(arr1)

    for i in range(y):
        x_list = []
        for j in range(x):
            mul = 0
            for k in range(len(arr1[0])):
                tmp1 = arr1[i][k]
                tmp2 = arr2[k][j]
                mul += tmp1 * tmp2
            x_list.append(mul)
        answer.append(x_list)

    return answer
