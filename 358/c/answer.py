N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]

buy_list=[0]*M
store_list=[]
for i in range(2**N):
    for j in range(N):
        if i>>j & 1:
            for idx,check in enumerate(S[j]):
                if check == 'o':
                    buy_list[idx] = 1
            
    if buy_list == [1]*M:
        store_list.append(bin(i).count('1'))
    buy_list = [0]*M
print(min(store_list))