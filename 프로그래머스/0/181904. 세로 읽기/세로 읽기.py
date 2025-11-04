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

# def solution(s, m, c):
#     return s[c-1::m]