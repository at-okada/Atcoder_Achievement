n = int(input())

def make_field(x):
    #とりまグリッドを縦横3**xマス'.'de全部埋める
    field = [['.']*(3**x) for _ in range(3**x)]
    if x == 0:
        return [['#']]
    print(x)
    #再帰関数
    old_field = make_field(x-1)
    print(old_field)
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                continue
            for k in range(3**(x-1)):
                for l in range(3**(x-1)):
                    field[3**(x-1)*i+k][3**(x-1)*j+l] = old_field[k][l]
    return field

field = make_field(n)
for x in field:
    print("".join(x))