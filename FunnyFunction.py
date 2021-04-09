size=21

abcCube=[[[0 for i in range(size)] for j in range(size)] for k in range(size)]

for a in range(0,size):
    for b in range(0, size):
        for c in range(0, size):
            if a==0 or b==0 or c==0:
                abcCube[a][b][c]=1

for a in range(0,size):
    for b in range(0, size):
        for c in range(0, size):
            if abcCube[a][b][c]==0:
                if a<b and b<c:
                    abcCube[a][b][c]=abcCube[a][b][c-1]+abcCube[a][b-1][c-1]-abcCube[a][b-1][c]
                else:
                    abcCube[a][b][c] = abcCube[a-1][b][c] + abcCube[a-1][b - 1][c]+ abcCube[a-1][b][c - 1] - abcCube[a-1][b - 1][c-1]
for a in range(0,size):
    print(a)
    for b in range(0, size):
        print(abcCube[a][b])
    print()