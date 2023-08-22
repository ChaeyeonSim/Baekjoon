# 복습요망

S = input()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0
for set in dial:
    for i in set:
        for x in S:
            if i == x:
                time += dial.index(set) + 3
print(time)