def solution(hp):
    answer = 0
    if hp%5==0:
        answer = hp//5
    elif hp%5==1:
        answer = hp//5 + (hp%5)//1
    elif hp%5==2:
        answer = hp//5 + (hp%5)//1
    elif hp%5==3:
        answer = hp//5 + (hp%5)//3
    elif hp%5==4:
        answer = hp//5 + (hp%5)//3 + ((hp%5)%3)//1
    return answer