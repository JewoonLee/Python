from sys import stdin
input = stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split()))
nlist = sorted(nlist)

def bifind(nlist,intm,s,e):
    mid = int((s + e) / 2)
    if s>=e:
        if s == e:
            if nlist[s] == intm:
                return 1
            else:
                return 0
        else:
            return 0
        
    else:
        if nlist[mid] == intm:
            return 1
        elif nlist[mid] < intm:
            return bifind(nlist,intm,mid + 1,e)
        elif nlist[mid] > intm:
            return bifind(nlist,intm,s,mid - 1)

for i in range(m):
    if bifind(nlist,mlist[i],0,n-1):
        print("1")
    else:
        print("0")