
chessBoard = [[0 for i in range(8)] for j in range(8)]

possibleMoves = [[1, 2], [2, 1],
               [-1, -2], [-2, -1],
               [-1, 2], [2, -1],
               [-2, 1], [1, -2]]

for item in chessBoard:
    print(item)