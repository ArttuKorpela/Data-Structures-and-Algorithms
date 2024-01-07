def primes(N):
    a = 0;
    for i in range(2,N+1):
        a += check(i)
    return a

def check(n):
    if n <= 1:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1

if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15