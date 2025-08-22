# def solution(a, b, flag):
#     answer = 0
    
#     if flag == True:
#         answer = a+b
#     else:
#         answer = a-b
#     return answer

############### flag문제 ###################

def solution(n):
    answer = 0
    ls = []
    c_ls = []
    
    numbers = str(n)
    ls.extend(numbers)
    
    for i in ls:
        c_ls.append(int(i))

    answer = sum(c_ls)

    return answer

print(solution(123))

# def solution(n):
#     numbers = str(n)     # 숫자를 문자열로 변환
#     c_ls = []            # 각 자리 정수를 저장할 리스트
    
#     for ch in numbers:   # 문자열의 각 문자를 순회
#         c_ls.append(int(ch))
    
#     answer = sum(c_ls)   # 리스트의 합
    
#     return answer

# print(solution(123)) 