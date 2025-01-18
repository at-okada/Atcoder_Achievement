N, M = map(int, input().strip().split())

count = [0] * N  

for _ in range(M):
    num, char = input().strip().split() 
    num = int(num)

    if char == "M":
        if count[num - 1] == 0: 
            print("Yes")
            count[num - 1] = 1 
        else:
            print("No")
    else:
        print("No")