N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# AとBを結合し、昇順にソートする
C = sorted(A + B)

# 2つの連続する要素がAに存在するかどうかを判定する
pairs = "No"
for i in range(len(C) - 1):
    # 連続する要素がAに存在する場合
    # in A で配列Aの中に値があるか調べることができるらしい
    if C[i] in A and C[i+1] in A:  
        pairs = "Yes"
        break

print(pairs)