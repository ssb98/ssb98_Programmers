def solution(age):
    answer = ''
    age_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
    # 딕셔너리의 키(알파벳)와 값(숫자)을 반전시켜, 숫자 -> 알파벳 매핑 딕셔너리 생성
    num_to_alpha = {v: k for k, v in age_dict.items()}
    
    # 입력받은 나이를 문자열로 변환 (예: 23 -> "23")
    age_str = str(age)
    
    # 문자열로 변환된 나이의 각 숫자를 순회
    for digit_char in age_str:
        # 각 숫자를 정수형으로 변환 (예: "2" -> 2)
        digit_int = int(digit_char)
        # 반전된 딕셔너리에서 해당 숫자에 대응하는 알파벳 찾기
        alpha = num_to_alpha[digit_int]
        # 결과 문자열에 추가
        answer += alpha
        
    return answer