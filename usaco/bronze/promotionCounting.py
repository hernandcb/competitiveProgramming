"""
 Promotion counting

 Easy ad-hoc problem from USACO
 http://www.usaco.org/index.php?page=viewproblem2&cpid=591
"""

fin = open("promote.in", "r")
fout = open("promote.out", "w")

a, a2 = [int(x) for x in fin.readline().split()]
b, b2 = [int(x) for x in fin.readline().split()]
c, c2 = [int(x) for x in fin.readline().split()]
d, d2 = [int(x) for x in fin.readline().split()]

dd = d2 - d
dc = c2 + dd - c
db = b2 + dc - b

fout.write(f"{db}\n")
fout.write(f"{dc}\n")
fout.write(f"{dd}\n")
