import math


def sums(A):
    possible_sums = {0}
    for num in A:
        new_sums = set()
        for s in possible_sums:
            new_sums.add(s + num)
        possible_sums.update(new_sums)

    return len(possible_sums) - 1


if __name__ == "__main__":
    print(sums([1, 2, 3]))  # 6
    print(sums([2, 2, 3]))  # 5
    print(sums([1, 3, 5, 1, 3, 5]))  # 18
    print(sums([1, 15, 5, 23, 100, 55, 2]))  # 121
