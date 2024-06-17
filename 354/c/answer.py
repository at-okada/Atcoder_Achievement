N = int(input())
AC = []

for i in range(N):
    a, c = map(int, input().split())
    AC.append((-a, c, i))

AC.sort()
cost = float("inf")
ok = []

#_,こいつは無視を意味する。この場合aを無視するという意味
for _, c, idx in AC:
    if c > cost:
        continue
    cost = c
    ok.append(idx + 1)

ok.sort()

print(len(ok))
print(*ok)