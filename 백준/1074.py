from sys import stdin
input = stdin.readline

Nrc = list(map(int,input().split()))

N = Nrc[0]
r = Nrc[1]
c = Nrc[2]

rows = 2 ** N
cols = 2 ** N


def makez(n,cs,ce,rs,re,start):

    global r
    global c
    N = 2 ** n
    smalln = 2 ** (n-1)
    smallnn = smalln * smalln

    
    while n != 0:
        N = 2 ** n
        smalln = 2 ** (n-1)
        smallnn = smalln * smalln
        if cs<=r<=cs + int(N / 2)-1:
            if rs <= c <= rs + int(N / 2)-1:
                n = n-1
                cs = cs
                ce = cs + int(N / 2)-1
                rs = rs
                re = rs + int(N / 2)-1
                start = start
                
            else:
                n = n-1
                cs = cs
                ce = cs + int(N / 2)-1
                rs = rs + int(N / 2)
                re = re
                start = start+ smallnn
        else:
            if rs <= c <= rs + int(N / 2)-1:
                n = n-1
                cs = cs + int(N / 2)
                ce = ce
                rs = rs
                re = rs + int(N / 2)-1
                start = start+ smallnn*2

            else:
                n = n-1
                cs = cs + int(N / 2)
                ce = ce
                rs = rs + int(N / 2)
                re = re
                start = start+ smallnn*3

    if n == 0:
        return start


anw = makez(N,0,cols-1,0,rows-1,0)

print(anw)





