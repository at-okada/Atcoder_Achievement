N = int(input())
A = list(map(int,input().split()))
T = 0
for a in A:
    num = a//5
    T += num*3
    a -= num*5
    while a>0:
        T+=1
        if T%3==0:
            a-=3
        else:
            a-=1

print(T)
