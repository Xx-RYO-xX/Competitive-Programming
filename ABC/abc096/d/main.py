import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import sympy

    n = int(input())
    prime = [i for i in sympy.sieve.primerange(55555)]

    for p in prime:
        if p % 5 == 1:
            print(p, end=" ")
            n -= 1
        if n == 0:
            return


if __name__ == "__main__":
    main()
