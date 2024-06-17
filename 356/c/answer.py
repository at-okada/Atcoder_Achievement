#bit全探索
N, M, K = map(int, input().split())

# 試した鍵のリスト
AA = []
# 鍵が開いたかどうかのリスト
R = []

for i in range(M):
    CAR = list(map(str, input().split()))
    # 各テストで試した鍵のリストを追加
    AA.append(list(map(int, CAR[1:-1])))
    # 各テストで鍵が開いたかどうかを追加
    R.append(True if CAR[-1] == "o" else False)

ans = 0


# とりあえず鍵のすべての組み合わせを試す (2^N 通り)
# if (R[j]) != (col >= K):ここで大体はじく
for i in range(1 << N):
    ok = True
    # 各テストケースを確認
    for j in range(M):
        # 各テストで正しい鍵の数を数える
        col = 0
        for a in AA[j]:
            # 鍵が現在の組み合わせに含まれる場合
            if (i & (1 << (a - 1))):
                col += 1
        # テスト結果が期待される結果と一致しない場合、矛盾とする
        if (R[j]) != (col >= K):
            ok = False
            break
    # すべてのテストが一致する場合、この組み合わせを有効と数える
    if ok:
        ans += 1

print(ans)      