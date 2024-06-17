# 入力を受け取る
N, T = map(int, input().split())
#全探索だと時間がかかるので
#マスを0から考えた方が楽
A = list(map(lambda x: int(x) - 1, input().split()))
row = [0] * N
col = [0] * N
#斜め
diag = [0] * 2

for i in range(T):
    #縦軸 仮にNが４の場合４以下が1行目
    x = A[i] // N
    #横軸 列
    y = A[i] % N


    #呼ばれた番号の行に対してカウントを1増やす
    row[x] += 1
    if row[x] == N:
        print(i + 1)
        exit()

    col[y] += 1
    if col[y] == N:
        print(i + 1)
        exit()

    if x == y:
        diag[0] += 1
        if diag[0] == N:
            print(i + 1)
            exit()

    if x + y == N-1:
        diag[1] += 1
        if diag[1] == N:
            print(i + 1)
            exit()

print(-1)
