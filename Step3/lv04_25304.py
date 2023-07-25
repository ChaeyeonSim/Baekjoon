X = int(input())
N = int(input())
total = 0

for i in range(N):
    a, b = map(int, input().split())
    c = a * b
    total += c

if (X == total):
    print("Yes")
else:
    print("No")