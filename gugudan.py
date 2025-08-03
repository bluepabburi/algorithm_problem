# choose = int(input('구구단 몇단을 계산할까요? : '))
# answer = 0
#
#  for i in range(1, 10):    
#     answer = choose * i
#     print(choose, 'X', i, '=', answer)

# ---------- 위(나)와 아래의 차이-----------

# print('구구단 몇단을 계산할까요? : ')
# dan = int(input())
# print(f'구구단 {dan}단을 계산합니다.')

# for i in range(1, 10):
#     print(f'{dan} X {i} = {dan*i}')



while(True):
    print('구구단 몇단을 계산할까요? : ')
    dan = int(input())
    
    if dan > 9 or dan < 1:
        print('구구단 게임을 종료합니다')
        break
        
    else:
        print(f'구구단 {dan}단을 계산합니다.')

        for i in range(1, 10): 
            print(f'{dan} X {i} = {dan*i}')

    