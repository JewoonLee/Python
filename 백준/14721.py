import numpy as np
from sys import stdin
input = stdin.readline

n = int(input())

M = np.zeros((n, 2))  # n행 2열의 영행렬 생성
R = np.zeros(n)

for i in range(n):
    x , y = (map(int,input().split()))
    M[i, 0] = x
    M[i, 1] = 1
    R[i] = y

inverse_M = np.linalg.pinv(M)

X = inverse_M @ R

a = round(X[0])
b= round(X[1])
print(a,b)