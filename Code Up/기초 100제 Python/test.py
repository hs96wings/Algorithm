d = []

for i in range(10):
    d.append(list(map(int, input().split())))

x = 1
y = 1
d[x][y] = 9

while True:
    if d[y][x+1] == 0 or d[y+1][x] == 0:
        if d[y][x+1] == 0:
            d[y][x+1] = 9
            x += 1
        else:
            d[y+1][x] = 9
            y += 1
    elif d[y][x+1] == 2 or d[y+1][x] == 2:
        if d[y][x+1] == 2:
            d[y][x+1] = 9
            break
        else:
            d[y+1][x] = 9
            break
    else:
        d[y][x] = 9
        break

for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()
