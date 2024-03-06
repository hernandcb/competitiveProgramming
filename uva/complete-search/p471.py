"""
Magic numbers

https://onlinejudge.org/external/4/471.pdf
tags: complete-search, easy
"""
import math

maxS = 9876543210

def has_repeated_digits(number):
  n_str = str(number)
  return len(set(n_str)) != len(n_str)


test = 0
cases = int(input())
_ = input()


while test < cases:
  if test > 0:
    input()
    print()

  N = int(input())
  test +=1

  for n2 in range(1, maxS):
    n1 = n2 * N

    if n1 > maxS:
      break

    if not has_repeated_digits(n1) and not has_repeated_digits(n2):
      print('{} / {} = {}'.format(n1, n2, N))