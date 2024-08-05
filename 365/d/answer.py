N = int(input())
S = input().strip()

win_map = {'R': 'P', 'P': 'S', 'S': 'R'}

old_hand = None
count = 0

for i in range(N):
    current_hand = win_map[S[i]]
    
    if current_hand == old_hand:
        if current_hand == 'R':
            current_hand = 'S'
        elif current_hand == 'P':
            current_hand = 'R'
        else:
            current_hand = 'P'

    if current_hand == win_map[S[i]]:
        count += 1
    
    old_hand = current_hand

print(count)