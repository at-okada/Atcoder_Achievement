import sys
N = int(input())
input = sys.stdin.read
data = input().strip().split()

l = 0

for name in data:
    if name == "Takahashi":
        l += 1
print(l)