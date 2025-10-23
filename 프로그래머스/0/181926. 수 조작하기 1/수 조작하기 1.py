def solution(n, control):
    for idx in control:
        if idx == 'w':
            n = n + 1
        elif idx == 's':
            n = n - 1
        elif idx == 'd':
            n = n + 10
        elif idx == 'a':
            n = n - 10
    return n