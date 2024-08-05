xa,ya = map(int, input().strip().split())
xb,yb = map(int, input().strip().split())
xc,yc = map(int, input().strip().split())

def is_right_triangle(x1, y1, x2, y2, x3, y3):

    def squared_distance(xa, ya, xb, yb):
        return (xa - xb) ** 2 + (ya - yb) ** 2

    a2 = squared_distance(x1, y1, x2, y2)
    b2 = squared_distance(x2, y2, x3, y3)
    c2 = squared_distance(x3, y3, x1, y1)

    return (a2 + b2 == c2) or (a2 + c2 == b2) or (b2 + c2 == a2)

if is_right_triangle(xa, ya, xb, yb, xc, yc):
    print("Yes")
else:
    print("No")