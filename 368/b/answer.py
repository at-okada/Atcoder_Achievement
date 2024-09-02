N = int(input().strip())
A = list(map(int, input().split()))

count = 0

while True:
    A.sort(reverse=True)
    
    positive_count = sum(1 for x in A if x > 0)
    
    if positive_count <= 1:
        break
    
    A[0] -= 1
    A[1] -= 1
    
    count += 1

print(count)