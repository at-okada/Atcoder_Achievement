S1, S2, S3 = input().strip().split()

A = 0
B = 0
C = 0

if S1 == "<":
    B += 1
else:
    A += 1

if S2 == "<":
    C += 1
else:
    A += 1

if S3 == "<":
    C += 1
else:
    B += 1

numbers_with_labels = [(A, 'A'), (B, 'B'), (C, 'C')]

numbers_with_labels.sort()

print(numbers_with_labels[1][1])
