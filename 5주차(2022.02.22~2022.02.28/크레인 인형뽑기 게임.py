def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        for j in range(len(board[1])):
            if board[j][i - 1] != 0:
                if len(stack) != 0 and stack[-1] == board[j][i - 1]:
                    stack.pop()
                    board[j][i - 1] = 0
                    answer += 2
                    break

                stack.append(board[j][i - 1])
                board[j][i - 1] = 0
                break

    return answer
