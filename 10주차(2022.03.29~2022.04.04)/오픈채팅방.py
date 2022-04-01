def solution(record):
    answer = []
    dic = {}
    result = []
    for i in record:
        tmp = i.split(" ")
        if tmp[0] == "Enter":
            dic[tmp[1]] = tmp[2]
            answer.append([tmp[1], "in"])
        elif tmp[0] == "Leave":
            answer.append([tmp[1], "out"])
        elif tmp[0] == "Change":
            dic[tmp[1]] = tmp[2]

    for i in answer:
        if i[1] == "in":
            result.append(dic[i[0]] + "님이 들어왔습니다.")
        elif i[1] == "out":
            result.append(dic[i[0]] + "님이 나갔습니다.")
    return result
