
def translator(num, width):
    if num == 0:
        return '0'.zfill(width)
    s = ""
    while num > 0:
        s = str(num % 2) + s
        num //= 2
    return s.zfill(width)


def solution(n, arr1, arr2):
    answer = []
    a1 = []
    a2 = []

    
    for i in range(n):
        a1.append(translator(arr1[i], n))
    for i in range(n):
        a2.append(translator(arr2[i], n))

    for i in range(len(a1)):
        row_list = list(a1[i])

        for j in range(len(row_list)):
            if row_list[j] == '1':
                row_list[j] = '#'
                a1[i] = ''.join(row_list)
            else:
                row_list[j] = ' ' 
                a1[i] = ''.join(row_list)
    
    for i in range(len(a2)):
        row_list = list(a2[i])

        for j in range(len(row_list)):
            if row_list[j] == '1':
                row_list[j] = '#'
                a2[i] = ''.join(row_list)
            else:
                row_list[j] = ' ' 
                a2[i] = ''.join(row_list)

    for r1, r2 in zip(a1, a2):                                                   # a1, a2 배열을 합치는 answer 구간 근데 도저히 이해가 안간다 지피티한테 물어본건데 이해가 ㅈㄴ 안간다 그냥 개빡친다 아
        merged = ''.join('#' if (c1 == '#' or c2 == '#') else ' '
                         for c1, c2 in zip(r1, r2))
        answer.append(merged)

    return a1, a2, answer


print(solution(5, [9, 22, 28, 18, 11], [30, 1, 21, 17, 28]))

# n x n의 배열을 가진 정사각형
# n개를 유지하기위한 패딩
# 둘 다 공백이면 공백, 둘 중 하나라도 벽이면 벽
# 리스트 주소 따라서 10진수 -> 2진수로 번역
# 벽은 1 공백은 0
# 리스트 번역하는 함수 제작해야함, 어떻게 만들지 고민 2의 n제곱을 사용하여 몫이 1이 아닐때 반복횟수를 x10하면 될듯

# a1[i][j] -> 문자열이라서 오류남 ㅆ^ㅂ

# zfill() 기억하자 패딩하는 방법

# .join -> '구분자'.join(리스트_또는_문자열_집합) 아니 근데 ^ㅂ 어떤 방식으로 작동하느거야 ㅈ같네 진짜 아 암아아아아ㅏㅇ매아ㅐㅁ아ㅐㅏ애압
# 아 눈 ㅈㄴ 아파 진짜 개 ㅈ같아 아ㅏㅏㅏㅏㅏㅏㅏ

# zip() -> 여러 시퀀스를 같은 인덱스끼리 묶어주는 함수