a, b, c, d, e, f = map(int, input().strip().split())
h, i, j, k, m, l = map(int, input().strip().split())

box1_x_range = (min(a, d), max(a, d))
box1_y_range = (min(b, e), max(b, e))
box1_z_range = (min(c, f), max(c, f))

box2_x_range = (min(h, k), max(h, k))
box2_y_range = (min(i, m), max(i, m))
box2_z_range = (min(j, l), max(j, l))

if (box1_x_range[1] <= box2_x_range[0] or box2_x_range[1] <= box1_x_range[0] or
    box1_y_range[1] <= box2_y_range[0] or box2_y_range[1] <= box1_y_range[0] or
    box1_z_range[1] <= box2_z_range[0] or box2_z_range[1] <= box1_z_range[0]):
    print("No")
else:
    print("Yes")