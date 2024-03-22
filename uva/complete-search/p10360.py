"""
 UVa 10360 - Rat Attack

 https://onlinejudge.org/external/103/10360.pdf
 tags: dynamic programming, 2D array, grid, sum area table
"""
grid_size = 1025

def solve(d, populations):
  total_deaths = []

  max_x = max_y = 0

  for x, y, _ in populations:
    max_x = max(max_x, x)
    max_y = max(max_y, y)

  # print(max_x, max_y)
  for x in range(max_x):
    for y in range(max_y):
      deads = 0

      for (rx, ry, n) in populations:
        if x-d <= rx <= x+d and y-d <= ry <= y+d:
          deads += n

      if deads > 0:
        total_deaths.append((x, y, deads))

  best_positions = sorted(total_deaths, key=lambda x: (x[2]), reverse=True)
  best = best_positions[0] if len(best_positions) > 0 else (0,0,0)

  print('{} {} {}'.format(best[0], best[1], best[2]))


tests = int(input())

for t in range(tests):
  if t > 0:
    input()

  d = int(input())
  n_populations = int(input())
  rat_populations = []

  for _ in range(n_populations):
    x, y, n = [int(r) for r in input().split()]
    rat_populations.append((x,y,n))

  sorted_populations = sorted(rat_populations, key=lambda x: (x[0], x[1]))
  solve(d, sorted_populations)
