"""
 Load balancing

 Complete search (hard) from USACO
 http://www.usaco.org/index.php?page=viewproblem2&cpid=617
"""
fin = open('balancing.in', 'r')
fout = open('balancing.out', 'w')

n, B = [int(x) for x in  fin.readline().split(' ')]



cows = []
X, Y = [], []
for _ in range(n):
  x, y = [int(x) for x in  fin.readline().split(' ')]
  cows.append((x, y))
  X.append(x+1)
  Y.append(y+1)

X.sort()
Y.sort()

m = len(cows)

for a in X:
  for b in Y:
    q1, q2, q3, q4 = 0, 0, 0, 0

    for cow in cows:
      if (cow[0] < a and cow[1] < b):
        q1 +=1
      elif (cow[0] < a and cow[1] > b):
        q2 +=1
      elif (cow[0] > a and cow[1] > b):
        q3 +=1
      else:
        q4 +=1


    m = min(max(q1, q2, q3, q4), m)
    # print(f'x: {a}, y: {b}', q1, q2, q3, q4, m)


fout.write(f'{m}\n')
