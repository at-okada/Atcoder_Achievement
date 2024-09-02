Q = int(input())
query = [input().strip().split() for _ in range(Q)]

bag = {}
count = 0

for i in range(Q):
    command = int(query[i][0])
    
    if command == 1:
        x = int(query[i][1])
        if x in bag:
            bag[x] += 1
        else:
            bag[x] = 1
            count += 1
    elif command == 2:
        x = int(query[i][1])
        if x in bag:
            bag[x] -= 1
            if bag[x] == 0:
                del bag[x]
                count -= 1
    elif command == 3:
        print(count)
