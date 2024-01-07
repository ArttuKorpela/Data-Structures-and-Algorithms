def recursion(x):
    if x == 0:
        return 1
    else:
        return recursion(x - 1) + recursion(x - 1)


for i in [0,1,10,15]:
    print(recursion(i))