import sys
import math

def input():return sys.stdin.readline().rstrip()


def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) +1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    prime = [i for i, val in enumerate(is_prime) if val]
    return prime


def main():
    n = int(sys.stdin.readline().rstrip())
    limit = int(math.sqrt(n)) +1
    prime = sieve(limit)
    
    count = 0
    for p in prime:
        p8 = p**8
        if p8 <= n:
            count +=1
        else:
            break

    m = len(prime)
    for i in range(m):
        p2 = prime[i]**2
        if p2 > n:
            break
        for j in range(i+1, m):
            q2 = prime[j]**2
            if p2 * q2 <= n:
                count +=1
            else:
                break

    print(count)

if __name__ == '__main__':
    main()
