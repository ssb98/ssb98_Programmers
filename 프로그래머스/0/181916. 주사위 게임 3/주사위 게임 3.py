def solution(a, b, c, d):
    answer = 0
    freq = {}
    
    for x in [a,b,c,d]:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    items = list(freq.items())  # [(값, 횟수), ...]
    
    if len(freq) == 1:
        p = items[0][0]
        answer = 1111 * p
    elif len(freq) ==2:
        if items[1][1] == 1:
            p = items[0][0]
            q = items[1][0]
            answer = (10*p+q)**2 
        elif items[0][1] ==1:
            q = items[0][0]
            p = items[1][0]
            answer = (10*p+q)**2
        elif items[1][1] == 2 and items[0][1] ==2 :
            p = items[0][0]
            q = items[1][0]
            answer = (p+q)*abs(p-q)
    elif len(freq) ==3:
        if items[0][1]==2 :
            p = items[0][0]
            q = items[1][0]
            r = items[2][0]
            answer = q*r
        elif items[1][1]==2 :
            q = items[0][0]
            p = items[1][0]
            r = items[2][0]
            answer = q*r
        elif items[2][1]==2 :
            q = items[0][0]
            r = items[1][0]
            p = items[2][0]
            answer = q*r
    elif len(freq) ==4:
        answer = min([a,b,c,d])
    return answer