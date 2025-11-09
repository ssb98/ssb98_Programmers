def solution(balls, share):
    #팩토리얼 구하는 함수 정의
    def factorial(n):
        fac = 1
        for i in range(1,n+1):
            fac *= i
        return fac
    
    # balls개 중에서 share개를 선택하는 경우의 수 
    answer = factorial(balls) / (factorial(balls - share)*factorial(share))
    return answer