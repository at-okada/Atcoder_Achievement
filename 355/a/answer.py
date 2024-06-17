a, c = map(int, input().split())

if a == c:
    print(-1)
else:
    value = {1,2,3}
    remain = value - {a,c}

    print(remain.pop())