def solution(my_string):
    for idx in 'aeiou':
        my_string = my_string.replace(idx,'')
    return my_string