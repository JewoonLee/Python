from sys import stdin
input = stdin.readline

n = int(input())
nlist = input()
nlist = nlist.split()
nlist = sorted(nlist)
nlist2=[]

for i in range(len(nlist)):
    nlist2.append(nlist[i])


m = int(input())
mlist =input()
mlist = mlist.split()



def bifind(nlist,intm,s,e):
    if s >= e:
        if s == e:
            if nlist[s] == intm:
                return s

            else:
                return -1
        else:
            return -1
    mid = int((s + e) / 2)

    if nlist[mid] != intm:
        if nlist[mid] < intm:
            return bifind(nlist,intm,mid + 1,e)

        elif nlist[mid] > intm:
            return bifind(nlist,intm,s,mid - 1)
    else:
        return mid

print(bifind(nlist2,mlist[3],0,9))


for i in range(m):
    nlist2 = []
    for j in range(len(nlist)):
        nlist2.append(nlist[j])
   
    count = 0
    while True:
        if bifind(nlist2,mlist[i],0,len(nlist2)-1) != -1:
            count+=1
            idx = bifind(nlist2,mlist[i],0,len(nlist2)-1)
            del nlist2[idx]
            continue
        else: 
            break
    
    print(count, end=" ")


