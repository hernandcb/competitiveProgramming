"""
 Milk measurement

 Simulation problem (hard) from USACO
 http://www.usaco.org/index.php?page=viewproblem2&cpid=761

 This is a solution provided in:
 https://usaco.guide/problems/usaco-761-milk-measurement/solution
"""

NAMES = ["Bessie", "Elsie", "Mildred"]
START_AMT = 7

with open("measurement.in") as read:
  update_num = int(read.readline())
  updates = []
  for _ in range(update_num):
    day, cow, change = read.readline().split(' ')
    updates.append((int(day), cow, int(change)))

updates.sort()

outputs = {c: START_AMT for c in NAMES}
display = NAMES.copy()

display_changes = 0

for u in updates:
  outputs[u[1]] += u[2]
  max_output = max(outputs.values())
  new_display = [name for name, o in outputs.items() if o == max_output]

  display_changes += display != new_display
  display = new_display


print(display_changes, file=open("measuremen.out", "w"))