# 복습 요망

numbers = []

for k in range(10):
    i = int(input())
    if i%42 not in numbers:
        numbers.append(i % 42)

print(len(numbers))