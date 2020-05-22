x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def center_point(x1, y1, x2, y2):
    if (int(abs(x1) + abs(y1))) <= (int(abs(x2) + abs(y2))):
        print(f"({int(x1)}, {int(y1)})")
    else:
        print(f"({int(x2)}, {int(y2)})")


center_point(x1, y1, x2, y2)
