def solution(n, arr1, arr2):
    answer = []
    binary_arr1 = []
    binary_arr2 = []
    result = []

    for i in range(n):
        b_arr1 = format(arr1[i], "b")
        b_arr2 = format(arr2[i], "b")
        k = ""

        if len(b_arr1) < n:
            b_arr1 = "0" * (n - len(b_arr1)) + b_arr1
        if len(b_arr2) < n:
            b_arr2 = "0" * (n - len(b_arr2)) + b_arr2

        for j in range(n):
            if b_arr1[j] == "1" or b_arr2[j] == "1":
                k += "#"
                continue
            if b_arr1[j] == "0" or b_arr2[j] == "0":
                k += " "
                continue
        result.append(k)

    return result
