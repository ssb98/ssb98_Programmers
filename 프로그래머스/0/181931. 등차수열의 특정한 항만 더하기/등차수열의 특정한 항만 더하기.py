def solution(a, d, included):
    answer = 0
    
    a_list = [a + d * i for i in range(len(included))]
    
    
    for idx, flag in enumerate(included):
        if flag:
            answer += a_list[idx]
    
    return answer