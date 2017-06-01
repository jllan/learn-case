def f(l, n):
    result = []
    for j in range(n-1, -1, -1):
        for k in range(j, n):
            result.append(l[k-j][k])
    for i in range(1, n):
        for k in range(0, n-i):
            result.append(l[k+i][k])
    return result

l1= [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
l2= [[1,  2,  3,  4,  5],
     [6,  7,  8,  9,  10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25]]
result = f(l2,len(l2))
print(result)
