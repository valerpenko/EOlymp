def Show(Board):
  for row in Board:
      for cell in row:
          if cell==X:
              print('X')
          elif cell == O:
              print('O')
          else:
              print(' ')
X=1
O=0
Empty=-1
Board=[[Empty,Empty,Empty],[Empty,Empty,Empty],[Empty,Empty,Empty]]
Show(Board)
