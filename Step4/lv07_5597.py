# 복습 요망

numbers = [False] * 30

for i in range(28):
    n = int(input())
    numbers[n - 1] = True

for i in range(30):
    if not numbers[i]:
        print(i + 1)