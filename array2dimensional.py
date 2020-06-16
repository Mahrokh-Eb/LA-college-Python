
m = 10
n = 3

a = [ ]
for i in range(m):
    row = [0] *n
    a += [row]

for i in range(m):
    for j in range(n):
        print( a[i][j], end=' ')
    print( )

a  = [[1,2], [3,4]] #sum two matrix
b = [[1,1], [1,1]]
c = [[1,1], [1,1]]
for i in range(n):
    for j in range(n):
        c[i][j] = a[i][j] + b[i][j]
        print(i, j, end=' ')