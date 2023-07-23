from sys import stdin
input = stdin.readline

Nrc = list(map(int,input().split()))

N = Nrc[0]
r = Nrc[1]
c = Nrc[2]

rows = N ** 2
cols = N ** 2
z = [[0 for j in range(cols)] for i in range(rows)]

def makez(n,cs,ce,rs,re):
    global z
    N = n ** 2

    if n != 1:
        makez(n-1,cs,cs + int(N / 2),rs,rs + int(N / 2))
        makez(n-1,cs,cs + int(N / 2) ,rs + int(N / 2)+1, re)
        makez(n-1,cs + int(N / 2) +1,ce,rs,rs + int(N / 2))
        makez(n-1,cs + int(N / 2)+1,ce,rs + int(N / 2)+1, re)
    else:
        








