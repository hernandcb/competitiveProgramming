"""
  UVa 750 -  8 Queens Chess Problem
  https://onlinejudge.org/external/7/750.pdf

  tags: backtracking, easy
"""

n = 8 # board size
solutions = []

def is_free(array, pos):
  return array[pos] == -1

def search(col, cols, diag1, diag2):
  if col == n:
    solutions.append([str(y+1) for y in cols])
    return

  for row in range(n):
    if not is_free(cols, col): # queen was already placed here
      search(col+1, cols, diag1, diag2)
      break
    elif row not in cols and is_free(cols, col) and is_free(diag1, col+row) and is_free(diag2, col-row+n-1):
      cols[col] = diag1[col+row] = diag2[col-row+n-1] = row
      search(col+1, cols, diag1,diag2)
      cols[col] = diag1[col+row] = diag2[col-row+n-1] = -1


datasets = int(input())
input()



test = 0
for _ in range(datasets):
  if test > 0:
    input() # blank line
    print()

  solutions = []
  cols, diag1, diag2 = [-1]*n, [-1]*(n+n-1), [-1]*(n+n-1)
  row, col = [int(a)-1 for a in input().split(' ')]

  cols[col] = diag1[row+col] = diag2[col-row+n-1]= row


  print("""SOLN       COLUMN\n #      1 2 3 4 5 6 7 8""")
  print()

  search(0, cols, diag1, diag2)
  for i, sol in enumerate(solutions):
    print("{: >2}      {}".format(str(i+1), ' '.join(sol)))

  test +=1