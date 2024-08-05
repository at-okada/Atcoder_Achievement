N = int(input())
A = list(map(int, input().split()))

first = float('-inf')
second = float('-inf')
first_index = -1
second_index = -1

for i in range(N):
    if A[i] > first:
        second = first
        second_index = first_index
        first = A[i]
        first_index = i
    elif first > A[i] > second:
        second = A[i]
        second_index = i

print(second_index)