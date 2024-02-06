"""
 Milk measurement

 Simulation problem (hard) from USACO
 http://www.usaco.org/index.php?page=viewproblem2&cpid=761
"""
fin = open('measurement.in', 'r')
fout = open('measurement.out', 'w')

n = int(fin.readline())

cows = ['Bessie', 'Elsie', 'Mildred']
changes = [[] for _ in range(3)]

for _ in range(n):
  day, name, delta = fin.readline().split(' ')
  value = int(delta[1]) * ((-1) if delta[0]=='-' else 1)

  changes[cows.index(name)].append((int(day), value))

changes[0].sort(key=lambda x: x[0])
changes[1].sort(key=lambda x: x[0])
changes[2].sort(key=lambda x: x[0])

productions = [[7] for _ in range(3)] # Production per day of each cow

for cow in cows:
  n_cow = cows.index(cow)
  for day, delta in changes[n_cow]:
    # Fill with the same value
    last_measurement = len(productions[n_cow])-1
    productions[n_cow] += [productions[n_cow][-1]]*(day-last_measurement)
    productions[n_cow][day] += delta

# Fill the rest of the logs
for i in range(3):
  productions[i] += [productions[i][-1]]*(100-len(productions[i]))

def winners(productions, day):
  max_of_day = max(productions[0][day], productions[1][day], productions[2][day])

  return [productions[x][day] == max_of_day for x in range(3)]


changes = 0
for day in range(1, 100):
  if winners(productions, day) != winners(productions, day-1):
    changes += 1


fout.write(f'{changes}\n')