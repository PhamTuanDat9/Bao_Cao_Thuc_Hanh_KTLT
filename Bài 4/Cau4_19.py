print("Pham Tuan Dat")
print("235752021610105")
def sieve_of_eratosthenes(max_num):
    primes = [True] * max_num
    p = 2
    while p**2 < max_num:
        if primes[p]:
            for i in range(p**2, max_num, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, max_num) if primes[p]]
P = tuple(sieve_of_eratosthenes(1000))
print(P)
