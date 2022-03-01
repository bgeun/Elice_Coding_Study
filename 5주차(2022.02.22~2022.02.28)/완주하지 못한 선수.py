def solution(participant, completion):
    answer = ""
    # for i in completion:
    #     if i in participant:
    #         participant.remove(i)
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()
