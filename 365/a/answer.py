N = int(input())
A = [input().strip() for _ in range(N)]

x = "Yes"

for i in range(N - 2):
    if A[i] == A[i + 1] == "sweet":
        x = "No"

print(x)
