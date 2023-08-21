T = int(input())

for _ in range(T):
    R, S = map(str, input().split())
    for s in S:
        print(int(R)*s, end="")
    print()