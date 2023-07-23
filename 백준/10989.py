from sys import stdin
input = stdin.readline

n = int(input())
num_list = [0] * 10001

for i in range(n):
    getn = int(input())
    num_list[getn] += 1

for i in range(10001):
    if num_list[i]!=0:
        for j in range(num_list[i]):
            print(i)


