import sys
input = sys.stdin.read

def f(n):
    return n * (n + 1) // 2

# 入力の処理
data = input().strip().split()
N = int(data[0])
A = list(map(int, data[1:]))

# 主なロジック
ans = N
pre = 0

for i in range(1, N - 1):
    if A[i] - A[i - 1] != A[i + 1] - A[i]:
        ans += f(i - pre)
        pre = i

ans += f(N - 1 - pre)

# 結果の出力
print(ans)