from random import *

count=0
for i in range(1,51):
    rand = randint(5,51)
    if 5<=rand<=15:
        print("[o]"+str(i)+"번째 손님 (소요시간 : "+str(rand)+")")
        count+=1
        
    else:
        print("[ ]"+str(i)+"번째 손님 (소요시간 : "+str(rand)+")")

print("총 탑승 승객: "+ str(count))
 

