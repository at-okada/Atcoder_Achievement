import sys

N = int(input())

if N % 400 == 0:
    print(366)
    sys.exit()

if N % 100 == 0:
    print(365)
    sys.exit()

if N % 4 == 0:
    print(366)
else:
    print(365)