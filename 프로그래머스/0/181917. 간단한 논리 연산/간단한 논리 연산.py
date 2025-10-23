def solution(x1, x2, x3, x4):
    answer = True
    state1 = True
    state2 = True
    
    if x1 != x2 :
        state1 = True
    elif x1== x2 == True:
        state1 = True
    else:
        state1 = False
        
    if x3 != x4 :
        state2 = True
    elif x3== x4 == True:
        state2 = True
    else:
        state2 = False
        
    if state1 == state2 ==True:
        answer = True
    else:
        answer = False
        
    return answer