
factorial_number = int(input('원하는 숫자를 입력해주세요: '))
sum = 1

for i in range(factorial_number):
    factorial = factorial_number - i
    sum *= factorial

print(sum)

