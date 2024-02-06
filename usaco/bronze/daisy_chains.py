"""
  Daisy chains

  Complete search problem (easy)
  http://www.usaco.org/index.php?page=viewproblem2&cpid=1060
"""

N = int(input())
flowers = [int(x) for x in input().rstrip().split(' ')]

photos = []
for j in range(1, N+1):
  for i in range(0, j-1):
    photos.append(flowers[i: j])


count = N
for photo in photos:
  avg = sum(photo)/len(photo)
  if avg in photo:
    count += 1

print(count)