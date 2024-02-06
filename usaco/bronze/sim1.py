r, s = [int(x) for x in input().split(' ')]
m, n, p, q = [int(x) for x in input().split(' ')]

ax, ay = 0, 0
bx, by = r, s
t = 0

while ax < bx and ay < by:
    ax, ay = ax+m, ay+n
    bx, by = bx-p, by-q
    t += 1

if ax == bx and ay == by:
    print(t)
else:
    print(-1)

