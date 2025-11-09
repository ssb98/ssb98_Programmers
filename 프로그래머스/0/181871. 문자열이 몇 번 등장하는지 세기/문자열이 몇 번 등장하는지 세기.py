def solution(myString, pat):
    answer = 0
    for i in range(len(myString) - len(pat) + 1):
        # 현재 인덱스부터 pat 길이만큼 부분 문자열을 슬라이싱하고, pat과 일치하는지 확인
        if myString[i:i + len(pat)] == pat:
            answer += 1
    return answer