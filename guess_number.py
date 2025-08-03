import random

question = random.randrange(1, 100)
answer = ''

while(True):
    
    answer = int(input('숫자를 맞춰보세요: '))

    if answer == question:
        print('정답입니다!')
        break

    else:
        print('틀렸습니다')

        if answer > question:
            print('숫자가 너무 큽니다')

        else:
            print('숫자가 너무 작습니다')
