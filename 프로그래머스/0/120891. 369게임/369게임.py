def solution(order):
    answer = 0
    order = str(order)
    for num in order:
        if num == '3':
            answer += 1
        elif num == '6':
            answer += 1
        elif num == '9':
            answer += 1
    return answer