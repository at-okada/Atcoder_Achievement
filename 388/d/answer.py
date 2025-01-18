import bisect

N = int(input())  # 座標の数
X = list(map(int, input().split()))  # 座標リスト
P = list(map(int, input().split()))  # 各座標にいる人数リスト
Q = int(input())  # クエリの数

# 累積和の計算
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + P[i]

# クエリ処理
for _ in range(Q):
    L, R = map(int, input().strip().split())  # クエリで範囲 [L, R] を取得
    
    # L 以上の最初のインデックスを取得
    left_index = bisect.bisect_left(X, L)
    # R 以下の最後のインデックスを取得
    right_index = bisect.bisect_right(X, R) - 1
    
    # クエリ範囲内の人数の合計を計算
    if left_index <= right_index:
        total = prefix_sum[right_index + 1] - prefix_sum[left_index]
    else:
        total = 0  
    
    print(total)