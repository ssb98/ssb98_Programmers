def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
 
def solution(a, b):
    b //= gcd(a, b)  
    primes = [2, 5]
    cnt = 2
    
    while b > 1:
        if b % cnt == 0:
            b //= cnt
            if cnt not in primes or cnt > 5:
                return 2
        else:
            cnt += 1
    return 1