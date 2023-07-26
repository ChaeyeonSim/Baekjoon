import sys

try:
    while True:
        line = sys.stdin.readline().strip()

        if not line:
            break

        a, b = map(int, line.split())

        print(a + b)

except KeyboardInterrupt:
    sys.exit(0)