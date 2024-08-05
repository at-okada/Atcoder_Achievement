s, t = input().strip().split()
len_s = len(s)

for w in range(1, len_s):
    for c in range(w):
        now = ""
        for i in range(c, len_s, w):
            now += s[i]
        
        if now == t:
            print("Yes")
            exit()

print("No")