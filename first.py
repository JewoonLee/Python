num = int(input())

numlst=[]
for i in range(1,num+1):
    num2=int(input())
    numlst.append(num2)


numlst2=list(range(1,num+1))
numlst3=numlst


result = []    # 원래 만들 것
stack= []    #거쳐가는 stack
re=[]

# while result!=numlst:
#     if len(stack) == 0:
#         re.append("+")
#         stack.append(numlst2[0])
#         del numlst2[0]
    
#     else:
#         if numlst[0]==stack[len(stack)-1]:
#             re.append("-")
#             result.append(int(numlst[0]))
#             stack.pop()
#             del numlst[0]
#             if result==numlst:
#                 break
#             continue
#         elif numlst[0]!=stack[len(stack)-1]:
#             if len(numlst2)==0:
#                 print("No")
#                 break
#             else:
#                 re.append("+")
#                 stack.append(numlst2[0])
#                 del numlst2[0]


while result!=numlst:
    if len(stack)!=0:
        if numlst[0]!= stack[len(stack)-1]:
            if len(numlst2)==0:
                print("NO")
                break
            else:
                re.append("+")
                stack.append(numlst2[0])
                del numlst2[0]
                continue

        else:
            re.append("-")
            result.append(int(numlst[0]))
            stack.pop()
            del numlst[0]
            continue
    elif len(numlst2)!=0:
        re.append("+")
        stack.append(numlst2[0])
        del numlst2[0]
    else:
        break



if len(result) == num:
    for i in re:
        print(i)

