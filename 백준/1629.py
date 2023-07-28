from sys import stdin
input = stdin.readline


a, b, c =(map(int,input().split()))

modlist = dict()

def getmod(a,b,c):
    global modlist
    if b not in modlist:
        if b == 2 or b ==1:
            modlist[b] = a**b % c
            return(a**b % c)
        else:
            if b % 2 == 0: 
                if int(b/2) in modlist:
                    modlist[b] = modlist[b/2] * modlist[b/2] % c 
                else:
                    b1 = int(b/2)
                    modlist[b] = getmod(a,b1,c)*getmod(a,b1,c) % c
            else:
                b1 = int(b/2)
                b2 = int(b/2)+1
                if b1 in modlist and b2 in modlist:
                    modlist[b] = modlist[b1] * modlist[b2] % c
                elif b1 in modlist and b2 not in modlist:
                    modlist[b] = modlist[b1] * getmod(a,b2,c) % c
                    
                elif b1 not in modlist and b2 in modlist:
                    modlist[b] = getmod(a,b1,c) * modlist[b2] % c
                    
                else:
                    modlist[b] = getmod(a,b1,c)*getmod(a,b2,c) % c

    return modlist[b]
                    


print(getmod(a,b,c))
