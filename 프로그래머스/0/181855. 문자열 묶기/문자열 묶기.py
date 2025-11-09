def solution(strArr):
    answer = 0
    dic = {}
    
    for i in range(len(strArr)):
        if len(strArr[i]) in dic.keys() : 
            dic[len(strArr[i])] += 1
        else : 
            dic[len(strArr[i])] = 1
    
    answer = max(dic.values())
    
    return answer