H, W, Q = map(int, input().strip().split())
A = [tuple(map(int, input().strip().split())) for _ in range(Q)]

flags = set()
flags.add((0, 0))
flags.add((0, W - 1))
flags.add((H - 1, 0))
flags.add((H - 1, W - 1))

for r, c in A:
    if (r, c) in flags:
        flags.remove((r, c))
    else:
        adjacent = [
            (r - 1, c), 
            (r + 1, c), 
            (r, c - 1), 
            (r, c + 1)
        ]
        
        for adj_r, adj_c in adjacent:
            if 0 <= adj_r < H and 0 <= adj_c < W:
                if (adj_r, adj_c) in flags:
                    flags.remove((adj_r, adj_c))
    
    print(flags)

remaining_flags = len(flags)

print(remaining_flags)
