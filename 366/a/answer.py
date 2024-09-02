N, T, A= map(int, input().strip().split())

if N - T < T:
    print("Yes")
elif N - A < A:
    print("Yes")
else:
    print("No")
