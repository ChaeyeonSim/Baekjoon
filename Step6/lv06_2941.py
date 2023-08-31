# 복습 요망

S = input()

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro:
    S = S.replace(i, 'a')

print(len(S))