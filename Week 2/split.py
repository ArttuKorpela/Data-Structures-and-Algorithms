def split(T):
    n = 0

    #for i in range(1,len(T)):
    #    if max(T[:i]) < min(T[i:]):
    #        n += 1

    n = len(T)

    # Step 1: Create min_right array
    min_right = [0] * n
    min_right[-1] = T[-1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], T[i])

    return min_right



if __name__ == "__main__":
    print(split([1,2,3,4,5]))       # 4
    print(split([5,4,3,2,1]))       # 0
    print(split([2,1,2,5,7,6,9]))   # 3
    print(split([1,2,3,1]))         # 0