def solution(myString):
    answer = []
    string = sorted(myString.split('x'))
    for a in string:
        if a != '':
            answer.append(a)
    return answer