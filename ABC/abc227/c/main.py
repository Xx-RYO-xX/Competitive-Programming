import sys
from numba import njit


def input(): return sys.stdin.readline().rstrip()

@njit
def solve(n):
    ans = 0
    max_a = int(n ** (1/3))
    while (max_a+1)**3 <= n: 
        max_a += 1
    while max_a**3 > n:       
        max_a -= 1

    for a in range(1, max_a+1):
        limit_b = n // a
        max_b = int(limit_b ** 0.5)
        while (max_b+1)**2 <= limit_b: 
            max_b += 1
        while max_b**2 > limit_b:      
            max_b -= 1

        for b in range(a, max_b+1):
            c_max = n // (a * b)
            if c_max < b:
                break
            ans += c_max - b + 1
    return ans


def main():
    n = int(input())
    print(solve(n))

if __name__ == '__main__':
    main()
