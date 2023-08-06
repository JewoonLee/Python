from sys import stdin
input = stdin.readline
from collections import deque



m,n=(map(int,input().split()))
line=-1
firstmatrix = [[0 for i in range(m)] for j in range(n)]

visit = [[0 for i in range(m)] for j in range(n)]


for i in range(n):
    firstmatrix[i] = list(map(int,input().split()))


print(firstmatrix)

for i in range(n): 
    num = -1
    if 1 in firstmatrix[i]:
        num = firstmatrix[i].index(1)
        line = i
        break
    
print(line, num)
if num == -1 and line == -1:
    days = -1

else:
    days = 0
    
    def tomato(line, num):
        q = deque()
        global firstmatrix ,n ,m, days, visit

        q.append([line,num])

        while q:
            visit[line][num] = 1
            firstmatrix[line][num] = 1
            change = 0
            line, num = q.popleft()
            days+=1
            if 1 <= line <= n-2 and 1 <= num <= m-2:
                if (firstmatrix[line-1][num] == 0 or 1) and (visit[line-1][num] == 0):
                    firstmatrix[line-1][num] = 1
                    visit[line-1][num] = 1
                    q.append([line-1,num])
                    change = 1

                if (firstmatrix[line+1][num] == 0 or 1) and (visit[line+1][num] == 0):
                    firstmatrix[line+1][num] = 1
                    visit[line+1][num] = 1
                    q.append([line+1,num])
                    change = 1

                if (firstmatrix[line][num-1] == 0 or 1) and (visit[line][num-1] == 0):
                    firstmatrix[line][num-1] = 1
                    visit[line][num-1] = 1
                    q.append([line,num-1])
                    change = 1

                if (firstmatrix[line][num+1] == 0 or 1) and (visit[line][num+1] == 0):
                    firstmatrix[line][num+1] = 1
                    visit[line][num+1] = 1
                    q.append([line,num+1])
                    change = 1
                
                if change == 0:

                    print("here1")
                    days = -1
                    return
                
            
            elif 1 <= line <= n-2 and num == 0:
                if (firstmatrix[line-1][num] == 0 or 1) and (visit[line-1][num] == 0):
                    firstmatrix[line-1][num] = 1
                    visit[line-1][num] = 1
                    q.append([line-1,num])
                    change = 1

                if (firstmatrix[line+1][num] == 0 or 1) and (visit[line+1][num] == 0):                   
                    firstmatrix[line+1][num] = 1
                    visit[line+1][num] = 1
                    q.append([line+1,num])
                    change = 1

                if (firstmatrix[line][num+1] == 0 or 1) and (visit[line][num+1] == 0):
                    firstmatrix[line][num+1] = 1
                    visit[line][num+1] = 1
                    q.append([line,num+1])
                    change = 1

                if change == 0:
                    print("here2")
                    days = -1
                    return
            
            elif 1 <= line <= n-2 and num == m-1:
                if (firstmatrix[line-1][num] == 0 or 1) and (visit[line-1][num] == 0):
                    firstmatrix[line-1][num] = 1
                    visit[line-1][num] = 1
                    q.append([line-1,num])
                    change = 1
                if (firstmatrix[line+1][num] == 0 or 1) and (visit[line+1][num] == 0):
                    firstmatrix[line+1][num] = 1
                    visit[line+1][num] = 1
                    q.append([line+1,num])
                    change = 1

                if (firstmatrix[line][num-1] == 0 or 1) and (visit[line][num-1] == 0):
                    firstmatrix[line][num-1] = 1
                    visit[line][num - 1]  = 1
                    q.append([line,num-1])
                    change = 1

                if change == 0:
                    print("here3")
                    days = -1
                    return

            elif line == 0 and 1<= num <= m - 2:
                if (firstmatrix[line][num-1] == 0 or 1) and (visit[line][num-1] == 0):
                    firstmatrix[line][num-1] = 1
                    visit[line][num-1] = 1
                    q.append([line,num-1])
                    change = 1

                if (firstmatrix[line][num+1] == 0 or 1) and (visit[line][num+1] == 0):
                    firstmatrix[line][num+1] = 1
                    visit[line][num+1] = 1
                    q.append([line,num+1])
                    change = 1

                if (firstmatrix[line+1][num] == 0 or 1) and (visit[line+1][num] == 0):
                    firstmatrix[line+1][num] = 1
                    visit[line+1][num] = 1
                    q.append([line+1,num])
                    change = 1

                if change == 0:
                    print("here4")
                    days = -1
                    return

            elif line == n-1 and 1<= num <= m - 2:
                if (firstmatrix[line][num-1] == 0 or 1) and (visit[line][num-1] == 0):
                    firstmatrix[line][num-1] = 1
                    visit[line][num-1] = 1
                    q.append([line,num-1])
                    change = 1

                if (firstmatrix[line][num+1] == 0 or 1) and (visit[line][num+1] == 0):
                    visit[line][num+1] = 1
                    firstmatrix[line][num+1] = 1
                    q.append([line,num+1])
                    change = 1

                if (firstmatrix[line-1][num] == 0 or 1) and (visit[line-1][num] == 0):
                    firstmatrix[line-1][num] = 1
                    visit[line-1][num] = 1 
                    q.append([line-1,num])
                    change = 1

                if change == 0:
                    print("here5")
                    days = -1
                    return
                
            elif line == 0  and num == 0:
                if (firstmatrix[line+1][num] == 0 or 1) and (visit[line+1][num] == 0):
                    firstmatrix[line+1][num] = 1
                    visit[line+1][num] = 1
                    q.append([line+1,num])
                    change = 1

                if (firstmatrix[line][num+1] == 0 or 1) and (visit[line][num+1] == 0):
                    firstmatrix[line][num+1] = 1
                    visit[line][num+1] = 1
                    q.append([line,num+1])
                    change = 1

                if change == 0:
                    print("here6")
                    days = -1
                    return
            
            elif line == n-1 and num == 0:
                if (firstmatrix[line-1][num] == 0 or 1) and (visit[line-1][num] == 0):
                    firstmatrix[line-1][num] = 1
                    visit[line-1][num] = 1 
                    q.append([line-1,num])
                    change = 1

                if (firstmatrix[line][num+1] == 0 or 1) and (visit[line][num+1] == 0):
                    firstmatrix[line][num+1] = 1
                    visit[line][num+1] = 1
                    q.append([line,num+1])
                    change = 1

                if change == 0:
                    print("here7")
                    print(visit[line][num+1])
                    print(visit[line-1][num])
                    days = -1
                    return
            
            elif line == 0 and num == m-1:
                if (firstmatrix[line+1][num] == 0 or 1) and (visit[line+1][num] == 0):
                    firstmatrix[line+1][num] = 1
                    visit[line+1][num] = 1
                    q.append([line+1,num])
                    change = 1

                if (firstmatrix[line][num-1] == 0 or 1) and (visit[line][num-1] == 0):
                    firstmatrix[line][num-1] = 1
                    visit[line][num-1] = 1
                    q.append([line,num-1])
                    change = 1

                if change == 0:
                    print("here8")
                    days = -1
                    return
                
            elif line == n-1 and num == m-1:
                if (firstmatrix[line-1][num] == 0 or 1) and (visit[line-1][num] == 0):
                    firstmatrix[line-1][num] = 1
                    visit[line-1][num] = 1
                    q.append([line-1,num])
                    change = 1

                if (firstmatrix[line][num-1] == 0 or 1) and (visit[line][num-1] == 0):
                    visit[line][num-1] = 1
                    firstmatrix[line][num-1] = 1
                    q.append([line,num-1])
                    change = 1

                if change == 0:
                    print("here9")
                    days = -1
                    return
                
            if visit.count(1) == n * m:
                break
                
                
tomato(line,num)

print(visit)
print(firstmatrix)

print(days)
