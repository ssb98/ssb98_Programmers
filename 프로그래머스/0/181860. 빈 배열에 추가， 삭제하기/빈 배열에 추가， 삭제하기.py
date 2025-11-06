def solution(arr, flag):
    answer = []
    X=[]
    for i in range(len(arr)):
        if flag[i] == True:
            for n in range(arr[i]*2):
                X.append(arr[i])
        elif flag[i] == False:
            for m in range(arr[i]):
                X.pop()
    return X