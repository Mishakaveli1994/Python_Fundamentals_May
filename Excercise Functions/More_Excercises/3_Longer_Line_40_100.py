def closer_point(x1, y1, x2, y2):
    closer_to_zero = False
    point1 = int(abs(x1) + abs(y1))
    point2 = int(abs(x2) + abs(y2))
    if point1 <= point2:
        closer_to_zero = True
    return closer_to_zero


def calc_length(x1, y1, x2, y2):
    line_len = int((x2 - x1) + (y2 - y1))
    return line_len


ax1 = float(input())
ay1 = float(input())
ax2 = float(input())
ay2 = float(input())
bx1 = float(input())
by1 = float(input())
bx2 = float(input())
by2 = float(input())

line1 = calc_length(ax1, ay1, ax2, ay2)
line2 = calc_length(bx1, by1, bx2, by2)
closer1 = closer_point(ax1, ay1, ax2, ay2)
closer2 = closer_point(bx1, by1, bx2, by2)

if line1 >= line2 and closer1 == True:
    print(f"({int(ax1)}, {int(ay1)})({int(ax2)}, {int(ay2)})")
elif line1 >= line2 and closer1 == False:
    print(f"({int(ax2)}, {int(ay2)})({int(ax1)}, {int(ay1)})")
elif line1 < line2 and closer2 == True:
    print(f"({int(bx1)}, {int(by1)})({int(bx2)}, {int(by2)})")
elif line1 < line2 and closer2 == False:
    print(f"({int(bx2)}, {int(by2)})({int(bx1)}, {int(by1)})")
