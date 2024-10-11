list = [
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,1,1,1]
    ]
print(list)
n=4
m=4
answear = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            answear[i][j] = True
        elif list[i][j] == 0:
            answear[i][j] = False
        else:
            if i == 1 and j != 1:
                answear[i][j] = answear[i][j-1]
            if i != 1 and j == 1:
                answear[i][j] = answear[i-1][j]
            if i!= 1 and j!= 1:
                answear[i][j] = answear[i][j-1] or answear[i-1][j]
print(answear[n-1][m-1])
for i in range(n):
    print(answear[i])
            