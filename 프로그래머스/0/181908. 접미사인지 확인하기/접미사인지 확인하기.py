def solution(my_string, is_suffix):
    answer = 0
    sum = []
    for i in range(len(my_string)):
        sum.append(my_string[i:])
        if is_suffix in sum:
            answer = 1
        else:
            answer = 0
    return answer