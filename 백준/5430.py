from sys import stdin
input = stdin.readline
import re

n = int(input())


array=[]


for i in range(n):
    reverse = 0
    arrayRD=list(input().rstrip())
    getn= int(input())
    getlist = input().rstrip()

    if getn == 0:
        getlist = []

    else:
        getlist = getlist.replace("[","")
        getlist = getlist.replace("]","")
        getlist = list(map(int, getlist.split(","))) 

    
    if arrayRD.count('D')>getn:
        array.append("error")        
        continue
    else:
        for i in range(len(arrayRD)):
            if arrayRD[i] == 'R':
                if reverse == 0 :
                    reverse = 1
                else:
                    reverse  = 0
            elif arrayRD[i] == 'D':
                if reverse == 0:
                    del getlist[0]
                else:
                    del getlist[len(getlist)-1]
        if reverse == 1:
            getlist.reverse()

        array.append(getlist)

for i in range(len(array)):
    awn = str(array[i])
    awn = awn.replace(" ","")
    print(awn)
