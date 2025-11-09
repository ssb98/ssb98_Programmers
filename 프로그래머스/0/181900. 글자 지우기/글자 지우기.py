def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:
            answer += my_string[i]
    return answer

## 지우는거 보다 해당 인덱스만 뽑아서 합치는 방식이 더 괜찮아 보임.