import sys
import math

mnlist = list(map(int, sys.stdin.readline().split()))
m = mnlist[0]
n = mnlist[1]


def sosu(n):
    condition = 1
    if n == 1:
        condition = 0
    elif n ==2:
        condition = 1
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                condition = 0
                break
    return condition
            


for i in range(m,n+1):
    if sosu(i):
        print(i)
    
