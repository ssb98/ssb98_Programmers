def solution(picture, k):
    # replace를 통해 기존의 값을 k배 한값으로 대체하여 반환
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer