def solution(myString):
    answer = []
    myString = myString.split('x')
    for str in myString:
        answer.append(len(str))
    return answer