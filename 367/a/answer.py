A,B,C= map(int, input().strip().split())

if C < B:
    C += 24
    A += 24

flag = 0

for i in range(B, C):
    if i == A:
        flag = 1

if flag == 1:
    print("No")
else:
    print("Yes")