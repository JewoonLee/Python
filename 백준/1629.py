from sys import stdin
input = stdin.readline


a, b, c =(map(int,input().split()))

modlist =[-1] * b

def getmod(a,b,c):
    global modlist
    if modlist[b] == -1:
        if b == 2 or 1:
            modlist[b] = a**b % c
        else:
            if b % 2 == 0: 
                b1 = int(b/2)
                getmod(a,b1,c)
                getmod(a,b1,c)
            else:
                b1 = int(b/2)
                b2 = int(b/2)+1
                getmod(a,b1,c)
                getmod(a,b2,c)
    else:
