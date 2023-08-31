White = [1, 1, 2, 2, 2, 8]

W = list(map(int, input().split()))

for i in range(6):
    print(White[i] - W[i], end=' ')