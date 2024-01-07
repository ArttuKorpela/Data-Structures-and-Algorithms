import math

count = [0]
def permutations(k, n, numbers, included):
    if k == n:
        count[0] += 1
        if count[0] == 80:
            print(numbers)
    else:
        for i in range(1, n+1):
            if not included[i]:
                included[i] = True
                numbers[k] = i
                permutations(k+1, n, numbers, included)
                included[i] = False

n = 5
numbers = [0] * n  # To hold the numbers forming the current permutation
included = [False] * (n+1)  # To keep track of included numbers, 1-indexed

permutations(0, n, numbers, included)

