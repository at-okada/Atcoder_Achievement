R, G, B= map(int, input().strip().split())
C = input().strip()

if C == "Red":
    print(min(G,B))
elif C == "Green":
    print(min(R,B))
else :
    print(min(R,G))