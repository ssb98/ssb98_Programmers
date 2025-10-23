def solution(num_list):
    answer = 0
    a = 1
    b = 0
    for i in num_list:
        a *= i
    for i in num_list:
        b += i 
    if a < b**2:
        answer = True
    else:
        answer = False
    return int(answer)