def solution(s1, s2):
    answer = 0
    for i in s1:
        for idx in range(len(s2)):
            if i == s2[idx]:
                answer += 1
    return answer