import bisect
N = int(input())

A = list(map(int, input().split()))
A.sort(reverse=False)

count = 0

for i in range(N):
    h = A[i] / 2
    #右から挿入位置
    p = bisect.bisect_right(A, h)
    #なければ０
    count += p

print(count)