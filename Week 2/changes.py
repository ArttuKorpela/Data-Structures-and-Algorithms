

def changes(A):
    n = 0
    for i in range(len(A)):
        if (i == 0):
            continue
        else:
            if (A[i] == A[i-1]):
                n += 1
                A[i] = None
    return n


if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2