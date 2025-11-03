def solution(myString):
    answer = ''
    for str in myString:
        if str == 'a' or str == 'A':
            answer += str.upper()
        else:
            answer += str.lower()
    return answer