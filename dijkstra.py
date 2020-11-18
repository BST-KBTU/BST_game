def find(map,x,y,x1,y1):
    a = []
    for i in range(len(map)):
        a.append([])
        for j in range(len(map[i])):
            a[-1].append(0)
    a[y][x] = 1
    k = 1
    walls = [0,6,7]
    if map[y1][x1] in walls:
        print("strange")
        return None, None

    while a[y1][x1] == 0:
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == k:
                    if i>0 and a[i-1][j] == 0 and map[i-1][j] not in walls:
                        a[i-1][j] = k+1
                    if j>0 and a[i][j-1] == 0 and map[i][j-1] not in walls:
                        a[i][j-1] = k+1
                    if i<len(a)-1 and a[i+1][j] == 0 and map[i+1][j] not in walls:
                        a[i+1][j] = k+1
                    if j<len(a[i])-1 and a[i][j+1] == 0 and map[i][j+1] not in walls:
                        a[i][j+1] = k+1
        k += 1

    cur_i = y1
    cur_j = x1
    k = a[cur_i][cur_j]
    while a[cur_i][cur_j] != 2:
        if cur_i > 0 and a[cur_i-1][cur_j] == k-1:
            cur_i -= 1
        elif cur_j > 0 and a[cur_i][cur_j-1] == k-1:
            cur_j -= 1
        elif cur_i < len(a)-1 and a[cur_i+1][cur_j] == k-1:
            cur_i += 1
        elif cur_j < len(a[i])-1 and a[cur_i][cur_j+1] == k-1:
            cur_j += 1
        k = a[cur_i][cur_j]

    return cur_j, cur_i