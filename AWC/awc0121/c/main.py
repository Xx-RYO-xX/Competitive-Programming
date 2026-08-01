def main():
    import sys

    input = sys.stdin.readline

    import sympy

    for _ in range(int(input())):
        n = int(input())
        m = n if sympy.isprime(n) else sympy.nextprime(n)
        print(m - n)


if __name__ == "__main__":
    main()
