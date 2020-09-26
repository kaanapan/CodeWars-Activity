def spiralize(size):
    spiral = [[1 for _ in range(size)]]
    spiral += [[1 if x == size-1 else 0 for x in range(size)] for _ in range(size - 2)]
    spiral += [[1 for _ in range(size)]]
    length = size - 2
    count = 2
    x, y = size - 1, 0
    x_d, y_d = -1, 0
    while length > 0:
        for _ in range(count):
            for m in range(length):
                spiral[x][y] = 1
                if m != length-1:
                    x, y = x + x_d, y + y_d
            x_d, y_d = change_dir(x_d, y_d)
        length -= 2
        if length == 2:
            count = 1
    return spiral

def change_dir(x,y):
    if x == -1 and y == 0:
        return 0, 1
    elif x == 0 and y == 1:
        return 1, 0
    elif x == 1 and y == 0:
        return 0, -1
    elif x == 0 and y == -1:
        return -1,0