"""
 Speeding ticket

 Simulation problem (easy) from USACO
 http://www.usaco.org/index.php?page=viewproblem2&cpid=568
"""

fin = open('speeding.in', 'r')
fout = open('speeding.out', 'w')

limits = []
bessie = []
over_speed = [0]*100

n, m = [int(x) for x in fin.readline().split(' ')]

for _ in range(n):
  length, speed_limit = [int(x) for x in fin.readline().split(' ')]
  limits += [speed_limit] * length

for _ in range(m):
  length, speed_limit = [int(x) for x in fin.readline().split(' ')]
  bessie += [speed_limit] * length

for i in range(100):
  over_speed[i] = bessie[i] - limits[i]

fout.write(f'{max(max(over_speed), 0)}\n')