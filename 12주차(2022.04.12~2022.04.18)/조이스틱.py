def solution(name):
    # print([ord(i) for i in name])
    arr = [
        min(ord(i) - ord("A"), 1 + ord("Z") - ord(i)) for i in name
    ]  # 상하 최소거리 구하여 저장
    print(arr)
    idx = 0
    answer = 0

    # 조이스틱 움직여 글자 완성하기
    while True:
        answer += arr[idx]
        arr[idx] = 0  # 이동이 끝났으면 값을 0으로 만듦

        # 모든 값이 0이 되면 글자가 완성되었으므로 답을 리턴
        if sum(arr) == 0:
            return answer

        left = 1  # 왼쪽과 오른쪽으로 움직일 거리
        right = 1
        # 이동해야 할 글자가 나올 때까지 반복
        while arr[idx - left] == 0:
            left += 1
        while arr[idx + right] == 0:
            right += 1

        # left, right 중 최소거리 구하여 다음 위치로 이동
        if right > left:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right


# 좌우로 움직이는 로직은 A는 움직일 필요가 없으므로 왼쪽으로 움직일 때 A가 아닌
# 글자가 나오는 거리와 오른쪽으로 움직일 때 A가 아닌 글자가 나오는 거리 중 최소 거리로
# 움직이면 된다.
