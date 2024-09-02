import itertools

N, K = map(int, input().strip().split())
R = list(map(int, input().split()))

ranges = [range(1, end + 1) for end in R]

combinations = list(itertools.product(*ranges))

filtered_sequences = [seq for seq in combinations if sum(seq) % K == 0]

for seq in filtered_sequences:
    print(" ".join(map(str, seq)))