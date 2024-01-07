
def isort(A):
    for i in range(len(A)):
        #print(i)
        if i == len(A)-1:
            break
        while A[i+1] < A[i] and i>=0:
            small = A[i+1];
            large = A[i]
            A[i] = small
            A[i+1] = large
            i -=1




if __name__ == "__main__":
    A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
    isort(A)
    print(A)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]