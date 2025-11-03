def solution(n): 
    answer = 0 
    pizza = [] 
    for i in range(1, 101):
        for j in range(1, 101):
            if n*i == 6*j:
                pizza.append(6*j)
                answer = min(pizza)//6 
    return answer