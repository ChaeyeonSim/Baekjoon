import sys

T = int(input())

for i in range(T):
    input_line = sys.stdin.readline().strip()
    numbers = input_line.split()
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    print(num1+num2)