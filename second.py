from sys import stdin
input = stdin.readline
n = int(input())

arrayRD=[]
rearray=[[0 for j in range(100000)] for i in range(n)]


for i in range(n):
    arrayRD = list(input())
    getn= int(input())
    getlist = list(input())
    if arrayRD.count('D')>getn:
        rearray[i]="error"        
        continue
    else:
        intlist=[]
        intcount=0
        for j in range(len(getlist)):
            if getlist[j].isdigit():
                intlist.append(int(getlist[j]))

        if arrayRD.count('R')%2!=0:
            intlist.reverse()

        for k in range(arrayRD.count('D')):
            del intlist[0]

        rearray[i]=intlist

for j in range(len(rearray)):
    print(rearray[j])

        
        
            
        




