N, K, X= map(int, input().strip().split())
A = list(map(int, input().split()))

A.insert(K ,X)

print(" ".join(map(str, A)))