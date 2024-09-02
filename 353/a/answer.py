import sys
N = int(input())
H = list(map(int, input().split()))

for i in range(0, N):
    if H[0] < H[i]:
        print(i + 1)
        sys.exit()

print(-1)