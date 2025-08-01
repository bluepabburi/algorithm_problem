def solution(k, m, score):
    if m <= 0:
        raise ValueError("한 박스에 담을 사과 수 m은 1 이상이어야 합니다.")
    if len(score) < m:
        return 0 

    score.sort(reverse=True)
    price = 0

    for i in range(m - 1, len(score), m):
        price += score[i] * m

    return price