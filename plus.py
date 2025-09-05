# 각 배열의 주소는 같다
# 배열 하나씩 꺼내서 true 나 false일 때 조건식을 사용해서 음수 양수 표현하면 될 것 같다
# 마지막에 더하기


def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = absolutes[i] *  -1

        else:
            pass

        answer = sum(absolutes)

    return answer

