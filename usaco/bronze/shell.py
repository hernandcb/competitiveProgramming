"""
 Shell game

 Easy ad-hoc problem from USACO
 http://www.usaco.org/index.php?page=viewproblem2&cpid=891
"""

fin = open('shell.in', 'r')
fout = open('shell.out', 'w')

n = int(fin.readline())

points_p1, points_p2, points_p3 = 0, 0, 0
guess_p1, guess_p2, guess_p3 = 1, 2, 3

for i in range(n):
    a, b, g = [int(x) for x in fin.readline().split(' ')]

    if guess_p1 == a:
        guess_p1 = b
    elif guess_p1 == b:
        guess_p1 = a

    if guess_p2 == a:
        guess_p2 = b
    elif guess_p2 == b:
        guess_p2 = a

    if guess_p3 == a:
        guess_p3 = b
    elif guess_p3 == b:
        guess_p3 = a


    points_p1 += 1 if guess_p1 == g else 0
    points_p2 += 1 if guess_p2 == g else 0
    points_p3 += 1 if guess_p3 == g else 0

fout.write(f'{max(points_p1, points_p2, points_p3)}\n')
