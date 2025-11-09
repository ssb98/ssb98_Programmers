def solution(myString, pat):
    answer = ''
    # for str in myString:
    #     if pat not in answer:
    #         answer += str
    #     elif str == pat:
    #         answer += str
    
    end = myString.rfind(pat)
    return myString[:end+len(pat)]