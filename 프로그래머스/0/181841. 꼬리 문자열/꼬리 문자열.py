def solution(str_list, ex):
    answer = ''
    for str in str_list:
        if ex not in str:
            answer += str
        else:
            answer += ''
    return answer