# 복습 요망

S = input().upper()

S_set = list(set(S))

cnt = []

for i in S_set:
    cnt.append(S.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(S_set[cnt.index(max(cnt))])

