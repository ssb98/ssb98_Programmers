def solution(my_string, m, c):
    answer = ''
    my = ''
    string=[]
    
    for i in my_string:
        my += i
        if len(my) == m:
            string.append(my)
            my = ''
            
    for j in string:
        answer += j[c-1]
        
    return answer

## 스트링을 m개씩 나눠서 남고, 인덱싱으로 c위치를 answer에 담기