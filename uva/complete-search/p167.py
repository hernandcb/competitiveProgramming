"""
  UVa 167 -  The sultan's successor
  https://onlinejudge.org/external/1/167.pdf

  tags: backtracking, 8-queens, easy
"""
size = 8
solutions = []


def is_free(arr, pos):
  return arr[pos] == -1

def search(col, cols, diag1, diag2):
  if col == size:
    solutions.append([(x,cols[x]) for x in range(size)])

  else:
    for row in range(size):
      if row not in cols and is_free(diag1, col+row) and is_free(diag2,col-row+size-1):
        cols[col] = diag1[col+row] = diag2[col-row+size-1] = row
        search(col+1, cols, diag1, diag2)
        cols[col] = diag1[col+row] = diag2[col-row+size-1] = -1

# Pre-calculate all the posible solutions
cols, diag1, diag2 = [-1]*size, [-1]*(size+size-1), [-1]*(size+size-1)
search(0, cols, diag1, diag2)


def calculate_scores(board):
  max_score = 0

  for solution in solutions:
    points = [board[x][y] for (x,y) in solution]
    max_score = max(max_score, sum(points))

  return max_score


N = int(input())
for nBoard in range(N):
  board = []
  for _ in range(size):
    board.append([int(x) for x in input().split()])


  score = calculate_scores(board)
  print('{: >5}'.format(score))
