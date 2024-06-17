H = int(input())
cnt = 0
plant = 0

while True:
    plant += 2 ** cnt
    cnt +=1
    if plant > H:
        break
        
print(cnt)