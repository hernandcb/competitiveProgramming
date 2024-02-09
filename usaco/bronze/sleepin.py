t = int(input())

# Still failing some test cases, eg. 1 2 2 3 1 1
# it returns 5 with the array [10]
# but the correct answer is 4 with array [5, 5]

def solve(periods):
  if len (periods) <= 1 or len(set(periods)) == 1:
    return 0

  max_value = max(periods)
  modifications = 0
  new_periods = []
  sum_previous = 0

  for i in range(len(periods)):
    if periods[i] + sum_previous >= max_value:
      new_periods.append(periods[i]+sum_previous)
      sum_previous = 0
    else:
      sum_previous += periods[i]
      modifications += 1

  if sum_previous > 0:
    new_periods[-1] += sum_previous

  return modifications + solve(new_periods)



for _ in range(t):
  n = int(input())
  periods = [int(i) for i in input().split(' ')]

  print(solve(periods))
