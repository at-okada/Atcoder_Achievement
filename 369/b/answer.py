N = int(input().strip())

left_moves = 0
right_moves = 0

current_left = None
current_right = None

for _ in range(N):
    position, direction = input().split()
    position = int(position)

    if direction == 'L':
        if current_left is not None:
            left_moves += abs(position - current_left)
        current_left = position
    elif direction == 'R':
        if current_right is not None:
            right_moves += abs(position - current_right)
        current_right = position

print(left_moves + right_moves)