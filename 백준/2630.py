from sys import stdin
input = stdin.readline

bluebox=0
wihte = 0

def boxcount(nlist, nfcol, necol, nfrow, nerow):
    global bluebox
    global wihte
    ncol = necol - nfcol + 1
    nrow = nerow - nfrow + 1
    ncount = ncol * nrow
    countone = 0
    countz = 0

    if ncol <= 0 or nrow <= 0:
        return

    for col in range(nfcol, necol):
        for row in range(nfrow, nerow):
            if nlist[col][row] == 1:
                countone += 1
            elif nlist[col][row] == 0:
                countz += 1

    if countone != ncount and countz != ncount:
        boxcount(nlist, nfcol, int(nfcol + ncol / 2), nfrow, int(nfrow + nrow / 2))
        boxcount(nlist, int(nfcol + ncol / 2), necol, nfrow, int(nfrow + nrow / 2))
        boxcount(nlist, nfcol, int(nfcol + ncol / 2), int(nfrow + nrow / 2), nerow)
        boxcount(nlist, int(nfcol + ncol / 2), necol, int(nfrow + nrow / 2), nerow)

    elif countone == ncount:
        bluebox += 1
    elif countz == ncount:
        wihte += 1


# def boxcount(nlist,nfcol,necol,nfrow,nerow):
#     global bluebox
#     global wihte
#     ncol = necol - nfcol + 1
#     nrow = nerow - nfrow +1
#     ncount = ncol * nrow 
#     countone=0
#     countz=0
        
#     for col in range(nfcol-1,necol):
#         for row in range(nfrow-1,nerow):
#             if nlist[col][row] == 1:
#                 countone+=1
#             elif nlist[col][row] == 0:
#                 countz+=1

#     if countone != ncount or countz != ncount :
#         boxcount(nlist,nfcol,int(necol/2),nfrow,int(nerow/2))
#         boxcount(nlist,int(necol/2)+1,necol,nfrow,int(nerow/2))
#         boxcount(nlist,nfcol,int(necol/2),int(nerow/2)+1,nerow)
#         boxcount(nlist,int(necol/2)+1,necol,int(nerow/2)+1,nerow)

#     elif nlist.count(1) == ncount:
#         bluebox+=1
#     elif nlist.count(0) == ncount:
#         wihte+=1




n = int(input())
nlist = [[0 for col in range(n)] for row in range(n)]

for i in range(n):
    getnline =  list(input())
    ncount = 0
    for j in range(len(getnline)):
        if getnline[j].isdigit():
            nlist[i][ncount] = int(getnline[j])
            ncount+=1


boxcount(nlist,1,n,1,n)
print(wihte)
print(bluebox)
