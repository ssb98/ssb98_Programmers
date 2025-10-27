def solution(my_string):
    answer = []
    for idx in my_string:
        if idx in '0123456789' :
            answer.append(int(idx))
    return sorted(answer)

# def solution(my_string):
#     answer = []
#     for i in my_string:
#         if i.isdigit():
#             answer.append(int(i))
#     answer.sort()
#     return answer