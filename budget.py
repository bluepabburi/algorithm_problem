# d에 부서마다 필요한 금액이 올라옴 / budget은 총 예산안
# 최대한 많은 부서의 금액을 지원해야하므로, 낮은 수부터 더하여서 출력하면 간단할 듯 함

# 배열은 오름차순으로 정리, 루프를 사용하여 배열 순서에 따라 더함
# 루프를 돌다가 예산안을 넘어간다면, 그때 반복횟수를 리턴하면 될듯하다.



def solution(d, budget):
    answer = 0
    total = 0
    sort_d = sorted(d)
   
    for i in sort_d:             # 각 부서의 예산안을 루프를 돌면서 더할 수 있도록 함
        if total + i < budget:  
            total += i              
            answer += 1          # 반복 횟수 추가

        elif total + i == budget:  # 총 예산과 각 부서 예산 합이 같을 경우
            total += i                   
            answer += 1         

            return answer         # 예산안에 도달했으니, 루프 멈춤
            
        else:                      # 예산 초과시 루프 멈춤
            break               
    
    return answer

print(solution([1, 2, 2, 2, 2], 6))