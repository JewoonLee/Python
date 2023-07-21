from sys import stdin
input = stdin.readline

bluebox = 0
wihte = 0

def boxcount(nlist,nfcol,necol,nfrow,nerow,n):
    global bluebox
    global wihte

    countone = 0
    countz = 0

    if necol<=nfcol or nerow<=nfrow:
        if necol < nfcol or nerow < nfrow:
            return
        elif necol == nfcol or nerow == nfrow:
            if nlist[nfcol][nfrow]==1:
                bluebox+=1
            elif nlist[nfcol][nfrow]==0:
                wihte +=1
        return
        
    for col in range(nfcol,necol+1):
        for row in range(nfrow,nerow+1):
            if nlist[col][row] == 1:
                countone+=1
            elif nlist[col][row] == 0:
                countz+=1

    if countone != n*n and countz != n*n:
        boxcount(nlist,nfcol,int(nfcol + n/2)-1,nfrow,int(nfrow + n/2)-1,int(n/2))
        boxcount(nlist,int(nfcol+ n/2),necol,nfrow,int(nfrow + n/2)-1,int(n/2))
        boxcount(nlist,nfcol,int(nfcol + n/2)-1,int(nfrow + n/2),nerow,int(n/2))
        boxcount(nlist,int(nfcol+ n/2),necol,int(nfrow + n/2),nerow,int(n/2))

    elif countone == n * n:
        bluebox+=1
        return
    elif countz == n * n:
        wihte+=1
        return


n = int(input())

nlist = [[0 for col in range(n)] for row in range(n)]

for i in range(n):
    getnline =  list(input())
    ncount = 0
    for j in range(len(getnline)):
        if getnline[j].isdigit():
            nlist[i][ncount] = int(getnline[j])
            ncount+=1



boxcount(nlist,0,n-1,0,n-1,n)

print(wihte)
print(bluebox)

print("changed")