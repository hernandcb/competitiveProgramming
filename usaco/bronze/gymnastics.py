"""
  Cow gymnastics
  complete search (medium)

  http://www.usaco.org/index.php?page=viewproblem2&cpid=963
"""

fin = open('gymnastics.in', 'r')
fout = open('gymnastics.out', 'w')

k, n = [int(x) for x in fin.readline().split(' ')]

better = {(i+1):set() for i in range(n)}

for i in range(k):
  ranking = [int(x) for x in fin.readline().split()]

  while ranking:
    cow = ranking.pop(0)
    if i == 0:
      better[cow].update(ranking)
    else:
      better[cow].intersection_update(ranking)


consistent = 0
for cow_list in better.values():
  consistent += len(cow_list)

fout.write(f'{consistent}\n')
