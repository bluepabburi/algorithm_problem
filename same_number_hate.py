# 배열 내 연속되는 중복 숫자는 없애야함


def solution(arr):
    answer = []
    for i in range(len(arr)):
        if not answer or answer[-1] != arr[i]: # answer가 비어있거나, 마지막 원소와 현재 원소가 다를 때만 추가
            answer.append(arr[i])
    return answer

