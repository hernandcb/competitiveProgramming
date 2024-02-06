"""
  Stuck in ruts

  Simulation problem (Hard)
  http://www.usaco.org/index.php?page=viewproblem2&cpid=1061

  Still not passing all test cases
"""
N = int(input())
cows = []
to_east = []
to_nord = []

for _ in range(N):
  direction, x, y = input().split(' ')
  cow = (int(x), int(y))
  cows.append(cow)
  if direction == 'E':
    to_east.append(cow)
  elif direction == 'N':
    to_nord.append(cow)

to_nord.sort()
to_east.sort(key=lambda x: (x[1], x[0]))

steps = {pos: float('inf') for pos in to_east+to_nord}


for cow_to_E in to_east:
  for cow_to_N in to_nord:
    dx, dy = cow_to_N[0]-cow_to_E[0], cow_to_E[1]-cow_to_N[1]

    if dx < 0 or dy < 0:
      pass
    elif dx == dy:
      pass
    elif dx < dy  and steps[cow_to_E] >= dy: # cow_to_N will be stoped in dy steps
      steps[cow_to_N] = dy
    elif dy < dx and steps[cow_to_N] >= dx:
      steps[cow_to_E] = dx


for cow in cows:
  print(steps[cow] if steps[cow] != float('inf') else 'Infinity')
# print([(cow, steps[cow]) for cow in cows])
# print(steps)