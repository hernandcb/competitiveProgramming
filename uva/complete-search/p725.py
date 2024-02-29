import math

test = 0
while True:
    n = int(input())
    if n == 0: break

    if test > 0:
      print()

    count = 0
    for n2 in range(1234, math.ceil(98766/n)+1):
      n1 = n * n2

      if n1 / n2 == n and len(set(str(n1)+str(n2).zfill(5))) == 10:
          print("{:05d} / {:05d} = {}".format(n1, n2, n))
          count +=1
    if count == 0:
      print('There are no solutions for {}.'.format(n))

    test += 1
