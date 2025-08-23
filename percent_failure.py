#   '실패율은 스테이지에 도달했으나 클리어 못한 플레이어' / '스테이지에 도달한 플레이어'
#   만약 실패율이 같다면 낮은 스테이지가 먼저 앞으로 오게 
#   결과적으로 실패율이 높은 스테이지부터 내림차순으로 배열을 만들면됨 
#   n+1 스테이지는 모든 스테이지를 클리어 했다는 의미, 따라서 마지막 리턴할 때 최댓값은 N으로 잡고 리턴하면 될듯함


#  도착한 플레이어와 클리어 못한 플레이어의 비교를 위해, count()와 리스트의 비교연산을 통해서 갯수를 도출하도록 하였음,   반복문을 통한 (j >= s) >= True 를 작성했지만 문법에 어긋남

#  실패율을 구하기 위해 리스트를 만들고 연산을 시켰으나 nonetype 오류가 발생, comparing = comparing.append(s.count(i) / arrive_player)  
#   ㄴ 전에도 했던 실수 append()는 리스트자체를 변환시키는 것이지 마지막에 none을 리턴하기 때문에 '=' 를 사용해선 안됨

#   for j, h in range(N) 두 가지의 변수를 반복하기위해 작성 그런데  'cannot unpack non-iterable int object' 라는 오류가 발생, unpack이라길래 패킹해야하는줄 알고 튜플로 작성했으나 똑같은 오류 발생
#    ㄴ 리스트 원소가 정수인데, 두 변수로 받음 --> 따라서 enumulate()와 같은 함수로 N값을 두 변수에 할당할 수 있도록 해야함\
#          ㄴ N이 int값이라 반응을 안함 -> 그럼 그냥 문자열로 바꿔서 len()를 사용해보기로함
#                ㄴ 애초에 리스트와 같은 반복 가능한 값이 필요했음, range() 사용
#                         ㄴ 애초에 코드를 잘못 작성했다, 각 스테이지당 리스트를 한번씩 돌아야하는데, 기존은 그냥 1개씩 대조하도록 작성했음

# 실패율까진 구했는데, 이후 스테이지 번호를 어떻게 값을 붙여야할지 고민,, 딕셔너리를 사용하면 괜찮을까 음 고민된다
#  ㄴ 딕셔너리로 묶은 다음 밸류값을 나열하기로함 -> 람다 사용

# 작성후 답 제출했는데 런타임 오류남.. 어디서 잘못된건지 체크
# 기존 N개의 스테이지에서 도달하지 못한 스테이지는 실패율을 0으로 처리해야하는데 거기서 런타임 오류가 난건가 싶음
#   ㄴ 수정했으나 계속 런타임 오류가 남
#    ㄴ 실패율 0을 따로 삽입했으나 오류가 남
#     ㄴ  comparing.insert(h-1, 0)   기존 44번 코드에서 도달 인원이 0일 때 예외처리한 것이 문제가 되어 추가했는데, 
#          이렇게 하면 기존 루프가 끝난뒤의 마지막 값이라 코드가 꼬인다고함,, 그래서 그냥 append(0) 쓰는게 맞다고함
#              ㄴ 답은 맞게 나왔는데 이젠 시간초과때문에 실패가 뜸 이건 많이 억울한데 아,,, 

def solution(N, stages):
    answer = []
    s = stages
    arrive_player  = 0
    comparing = []
    dic_answer = {}

    for i in range(N):
        for h in range(len(stages)):        # 스테이지는 1부터 시작하는 것을 생각해, 리스트 값 하나하나 대조해보도록 함
            if ((i+1) <= s[h]):
                arrive_player += 1                               #  스테이지 도달한 플레이어 계산

        if arrive_player != 0:                     
            comparing.append(s.count(i+1) / arrive_player)      # 도달한 플레이어가 없을 수 있으니 예외처리

        else:
            comparing.append(0)                           # N값이 많을 때 딕셔너리에 할당할 리스트가 부족해서 에러 발생, 따라서 값을 추가할 수 있도록함
        
        arrive_player = 0


    for i, j in enumerate(range(N), start=1):                     # 각 스테이지 번호를 매길 수 있게 함
        dic_answer[i] = comparing[j]


    dic_answer = sorted(dic_answer.items(), key=lambda x: (-x[1], x[0]))       # 딕셔너리에서 밸류값을 통한 내림차순으로 분류
    dic_answer = dict(dic_answer)                                              # 튜플 값으로 나열된 것을 다시 딕셔너리로 바꿔줌


    answer = list(dic_answer.keys())                                      # 스테이지 단게인 키 값만 호출


    return answer



print(solution(5 ,[2, 1, 2, 6, 2, 4, 3, 3]))