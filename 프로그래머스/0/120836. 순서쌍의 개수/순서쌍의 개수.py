def solution(n):
    answer = 0
    a = range(1, n+1)
    for b in a:
        if n % b == 0:
            answer += 1
    return answer