import sys
from collections import Counter
 
n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))
 
dic = dict()
 
for i in n_arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
 
print(dic)
for i in range(m):
    if m_arr[i] in dic:
        print(dic[m_arr[i]], end=' ')
    else:
        print(0, end=' ')