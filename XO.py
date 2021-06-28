def Show(Board):
  for row in Board:
      for cell in row:
          if cell==X:
              print('X', end='')
          elif cell == O:
              print('O', end='')
          else:
              print('e ', end='')
      print()
X=1
O=0
Empty=-1
Board=[[Empty,Empty,Empty],[Empty,Empty,Empty],[Empty,Empty,Empty]]
Show(Board)
