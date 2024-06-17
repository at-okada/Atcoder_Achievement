N,L,R = map(int, input().split())

sequence = list(range(1, N + 1))

L -= 1
R -= 1

sequence[L:R+1] = sequence[L:R+1][::-1]

print(*sequence)