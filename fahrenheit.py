def convert(tmp1):

    Fahrenheit = ((9/5) * tmp1) + 32
    
    return Fahrenheit

print('본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.')

tmp = float(input('변환하고 싶은 섭씨 온도를 입력해주세요: '))

print('섭씨온도: ' , tmp)
print('화씨온도: ',f'{convert(tmp):5.2f}')

print(f'화씨온도: {convert(tmp): .2f}')