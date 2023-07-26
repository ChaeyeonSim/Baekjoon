N, M = map(int, input().split())

numbers = []

for k in range(N):
    numbers.append(k+1)

for k in range(M):
    i, j = map(int, input().split())
    numbers[i-1], numbers[j-1] = numbers[j-1], numbers[i-1]

print(*numbers)