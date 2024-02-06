"""
  Maximum distance

  Complete search (easy) - codeforce
  https://codeforces.com/gym/102951/problem/A
"""

def distance_square(a, b):
  distance = (b[0]-a[0])**2 + (b[1] - a[1])**2
  return distance

N = int(input())
X = [int(x) for x in input().rstrip().split(' ')]
Y = [int(x) for x in input().rstrip().split(' ')]
points = list(zip(X, Y))

max_distance = 0

for point1 in points:
  for point2 in points:
    distance = distance_square(point1, point2)
    max_distance = max(max_distance, distance)


print(max_distance)
