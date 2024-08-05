import bisect

N, Q = map(int, input().strip().split())
A = list(map(int, input().split()))
BQ = [tuple(map(int, input().strip().split())) for _ in range(Q)]

results = []

for b, q in BQ:
    # 二分探索で`b`の位置を見つける
    pos = bisect.bisect_left(A, b)
    
    # `b`に最も近い位置を探す
    closest_values = []
    
    if pos < N:
        closest_values.append((abs(A[pos] - b), A[pos]))
    if pos > 0:
        closest_values.append((abs(A[pos - 1] - b), A[pos - 1]))
    
    # `closest_values`を距離でソート
    closest_values.sort()
    
    # `q`番目に小さい距離を取得
    if len(closest_values) >= q:
        distance = closest_values[q - 1][0]
    else:
        distance = float('inf')  # または他の適切なデフォルト値
    
    results.append(distance)

# 結果を出力
print('\n'.join(map(str, results)))
