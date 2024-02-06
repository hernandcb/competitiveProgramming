"""
 Mixing milk

 Simulation problem (easy) from USACO
 http://www.usaco.org/index.php?page=viewproblem2&cpid=855
"""

fin = open('mixmilk.in', 'r')
fout = open('mixmilk.out', 'w')

c1, m1 = [int(x) for x in fin.readline().split(' ')]
c2, m2 = [int(x) for x in fin.readline().split(' ')]
c3, m3 = [int(x) for x in fin.readline().split(' ')]

contents = [m1, m2, m3]
capacities = [c1, c2, c3]

for n in range(100):
  bucket_a = n % 3
  bucket_b = (n+1) % 3

  amount = min(contents[bucket_a], capacities[bucket_b]-contents[bucket_b])

  contents[bucket_a] = contents[bucket_a] - amount
  contents[bucket_b] = contents[bucket_b] + amount

fout.write(f'{contents[0]}\n')
fout.write(f'{contents[1]}\n')
fout.write(f'{contents[2]}\n')