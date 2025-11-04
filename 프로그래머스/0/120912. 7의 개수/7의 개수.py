def solution(array):
    answer = 0
    for a in array:
        if '7' in str(a):
            answer += str(a).count('7')
    return answer