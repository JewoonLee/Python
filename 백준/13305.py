from sys import stdin
input = stdin.readline

n = int(input())

citydistance = list(map(int,input().split()))
cityprice = list(map(int,input().split()))

citycount = 0
realdis = 0
nowdis = 0 
realprice = 0
countdis = 0

for i in citydistance:
    realdis += i


count = 0

while citycount != n-1:
    nowdis = 0 
    for i in range(citycount+1,n):
        if cityprice[citycount] >= cityprice[i]:
            nowdis += citydistance[i-1]
            countdis += citydistance[i-1]
            realprice += nowdis*cityprice[citycount]
            citycount += i - citycount
            if countdis == realdis:
                citycount = n-1
            break
        else:
            nowdis += citydistance[i-1] 
            countdis += citydistance[i-1]
            if countdis == realdis:
                realprice += nowdis*cityprice[citycount]
                citycount = n-1
                break


print(realprice)