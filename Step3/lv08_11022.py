T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    sum = a + b
    print("Case #%d: %d + %d = %d" %((i+1), a, b, sum))