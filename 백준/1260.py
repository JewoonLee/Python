from sys import stdin
input = stdin.readline
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q :
        v = q.popleft()
        print(v,end =" ")
        for i in range(1,n+1):
            if matrix[v][i] == 1 and visit_list[i] == 0:
                q.append(i)
                visit_list[i] = 1

def dfs(v):
    visit_list2[v] = 1
    print(v, end = " ")
    for i in range(1,n + 1):
        if visit_list2[i] == 0 and matrix[v][i] == 1:
            dfs(i)




n , m , v =(map(int,input().split()))

matrix = [[0 for j in range(n+1)]for i in range(n+1)]

visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  matrix[a][b] = matrix[b][a] = 1

dfs(v)
print()
bfs(v)



