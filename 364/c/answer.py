H, W = map(int, input().strip().split())
Si, Sj = map(int, input().strip().split())

map_data = [input().strip() for _ in range(H)]

X = input().strip()

Si -= 1
Sj -= 1

for move in X:
    if move == "L" and Sj > 0 and map_data[Si][Sj - 1] == ".":
        Sj -= 1
    elif move == "R" and Sj < W - 1 and map_data[Si][Sj + 1] == ".":
        Sj += 1
    elif move == "U" and Si > 0 and map_data[Si - 1][Sj] == ".":
        Si -= 1
    elif move == "D" and Si < H - 1 and map_data[Si + 1][Sj] == ".":
        Si += 1

print(Si + 1, Sj + 1)