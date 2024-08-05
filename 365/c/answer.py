N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

total_sum = sum(A)

if total_sum <= M:
    print("infinite")
else:
    left, right = 0, max(A)
    best_x = 0

    while left <= right:
        mid = (left + right) // 2
        total = sum(min(mid, a) for a in A)
        print(total,best_x)
        if total <= M:
            best_x = mid
            left = mid + 1
        else:
            right = mid - 1

    print(best_x)