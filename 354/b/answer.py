N = int(input())

data = []

while True:
    try:
        line = input().strip()
        if not line:
            break
        row = line.split()
        data.append(row)
    except EOFError:
        break

data.sort()

mod = sum(int(item[1]) for item in data) % N

print(data[mod][0])
