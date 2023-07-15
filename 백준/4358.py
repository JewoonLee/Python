from sys import stdin
input = stdin.readline
trees = []

while True:
    tree = input().rstrip()
    if tree :
        trees.append(tree)
    else:
        break

trees = sorted(trees)
tree_count = len(trees)

nowtree = 1

for i in range(0,tree_count-1):
    
    if trees[i] == trees[i+1] and i != tree_count-2:
       nowtree += 1

    elif trees[i] == trees[i+1] and i == tree_count-2:
        nowtree += 1
        nowtree_p = nowtree / tree_count
        nowtree_p = nowtree_p*100
        print("{0} {1:.4f}".format(trees[i],nowtree_p))

    else:
        nowtree_p = nowtree / tree_count
        nowtree_p = nowtree_p*100
        if i+1 == tree_count-1:
            print("{0} {1:.4f}".format(trees[i],nowtree_p))
            nowtree_p = 1 / tree_count
            nowtree_p = nowtree_p*100
            print("{0} {1:.4f}".format(trees[i+1],nowtree_p))
        else:
            print("{0} {1:.4f}".format(trees[i],nowtree_p))
            nowtree = 1



        








    