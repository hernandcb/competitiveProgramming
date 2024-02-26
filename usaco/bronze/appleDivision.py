"""
Apple Division
Generating subsets (very easy)

https://cses.fi/problemset/task/1623
"""

n = int(input())
weights = list(map(int, input().split()))
# n = 3
# weights = [3, 2, 1]

groups = [(weights[0], 0)]

for p in weights[1: ]:
  new_groups = []
  for g in groups:
    new_groups.append((g[0]+p, g[1]))
    new_groups.append((g[0], g[1]+p))

  groups = new_groups

# print(groups)

differences = [abs(g[1]-g[0]) for g in groups]
print(min(differences))
