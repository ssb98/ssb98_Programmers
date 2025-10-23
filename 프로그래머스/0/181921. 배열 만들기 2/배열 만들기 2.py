def solution(l, r):
    answer = []
    for num in range(l, r+1):
        num_str = str(num)
        if all(char in'05' for char in num_str):
            answer.append(int(num_str))
    if len(answer) ==0:
        answer.append(-1)
    return answer