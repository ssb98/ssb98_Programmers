def solution(n):
    answer = 0
    num=[]
    for j in range(4, n+1):
        for i in range(1, n+1):
            if j % i == 0:
                num.append(j)
        if num.count(j) >= 3:
            answer +=1
    return answer