def solution(arr, queries):
    for i in range(len(queries)):
        s = queries[i][0]
        e = queries[i][1]
        for idx in range(s,e+1):
            arr[idx] += 1
    return arr