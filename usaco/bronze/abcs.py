"""
 Ad-hoc easy problem from USACO
 http://www.usaco.org/index.php?page=viewproblem2&cpid=1059
"""

numbers = [int(x) for x in input().split(' ')]
numbers.sort()

a = numbers[0]
b = numbers[1]

if (numbers[2] != a+b):
    c = numbers[2]
else:
    c = numbers[3]

print(a, b, c)

