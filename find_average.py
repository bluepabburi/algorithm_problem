def solution(arr):
    answer = 0
    
    sum_matrix = sum(arr)
    arr_length = len(arr)
    answer = sum_matrix / arr_length
    
    return answer


print(solution([1, 2, 3, 4]))