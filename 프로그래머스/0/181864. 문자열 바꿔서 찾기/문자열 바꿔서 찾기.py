def solution(myString, pat):
    answer = ''
    for idx in myString:
        if idx == 'A':
            answer += 'B'
        elif idx == 'B':
            answer += 'A'
    if pat in answer:
        return 1
    else:
        return 0