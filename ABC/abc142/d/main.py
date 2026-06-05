import sys


def input():
    return sys.stdin.readline().rstrip()


##https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    from math import gcd
    from sympy import isprime

    a, b = map(int, input().split())

    kouyakusu = make_divisors(gcd(a, b))
    print(sum(isprime(x) for x in kouyakusu) + 1)


if __name__ == "__main__":
    main()
