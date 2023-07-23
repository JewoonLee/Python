from sys import stdin
input = stdin.readline


n = int(input())

nlist = []
for i in range(n):
    getn = int(input())
    nlist.append(getn)



nlist = sorted(nlist)

for i in nlist:
    print(i)