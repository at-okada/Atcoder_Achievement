S = input().strip()
T = input().strip()

changes = 0
history = []
length = len(S)

i = 0
while S != T:
    while i < length:
        if S[i] != T[i]:
            if S[i] < T[i]:
                i += 1
                continue

            S = S[:i] + T[i] + S[i+1:]
            changes += 1
            history.append(S)

        i += 1

    i = length - 1
    while i >= 0:
        if S[i] != T[i]:
            if S[i] > T[i]:
                i -= 1
                continue

            S = S[:i] + T[i] + S[i+1:]
            changes += 1
            history.append(S)

        i -= 1

print(changes)
for s in history:
    print(s)