def solution(arr, intervals):
    answer = []
    [a1, b1] = intervals[0]
    [a2, b2] = intervals[1]
    arr1 = arr[a1: b1+1]
    arr2 = arr[a2: b2+1]
    
    answer = arr1+arr2
    return answer