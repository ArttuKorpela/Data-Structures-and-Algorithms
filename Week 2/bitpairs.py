def pairs(s):
    p = []

    for i in range(len(s)):
        if s[i] == "1":
            p.append(i)

    prefix_sum = 0
    result = 0

    for j, val in enumerate(p):
        result += j * val - prefix_sum
        prefix_sum += val

    return result




if __name__ == "__main__":
    print(pairs("100101"))          # 10
    print(pairs("101"))             # 2
    print(pairs("100100111001"))    # 71