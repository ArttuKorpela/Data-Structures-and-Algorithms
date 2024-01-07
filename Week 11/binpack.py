def binpack(items, S):
    sorted_items = sorted(items, reverse=True)
    ans = []

    for item in sorted_items:
        placed = False
        for bin in ans:
            if sum(bin) + item <= S:
                bin.append(item)
                placed = True
                break

        if not placed:
            ans.append([item])

    return ans


# Example usage
items = [5, 7, 8, 2, 3, 4, 6]
bin_size = 10
print(binpack(items, bin_size))


if __name__ == "__main__":

    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(items, B)

    for i in range(len(bins)):
        print(f"bin {i + 1}: {bins[i]}")

# A possible output:
#   bin 1: [9]
#   bin 2: [3, 3, 4]
#   bin 3: [6, 3]
#   bin 4: [10]
#   bin 5: [6]
#   bin 6: [8]
#   bin 7: [6]