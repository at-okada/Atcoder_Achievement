import sys
input = sys.stdin.read

# 入力処理
data = input().strip().split()
idx = 0

# 頂点数
N = int(data[idx])
idx += 1

# グラフGの辺
MG = int(data[idx])
idx += 1
edges_g = set()
for _ in range(MG):
    U = int(data[idx])
    V = int(data[idx + 1])
    idx += 2
    edges_g.add((min(U, V), max(U, V)))

# グラフHの辺
MH = int(data[idx])
idx += 1
edges_h = set()
for _ in range(MH):
    A = int(data[idx])
    B = int(data[idx + 1])
    idx += 2
    edges_h.add((min(A, B), max(A, B)))

# コスト行列の読み取り
costs = []
for _ in range(N - 1):
    costs.append(list(map(int, data[idx:idx + (N - _ - 1)])))
    idx += (N - _ - 1)

# 最小コストの計算
total_cost = 0

# 辺のコストを計算
for i in range(1, N):
    for j in range(i + 1, N + 1):
        cost = costs[i - 1][j - i - 1]  # コスト行列のインデックス計算
        if (i, j) in edges_g and (i, j) not in edges_h:
            total_cost += cost
        elif (i, j) not in edges_g and (i, j) in edges_h:
            total_cost += cost

# 結果の出力
print(total_cost)


