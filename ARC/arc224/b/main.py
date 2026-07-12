def main():
    import sys

    input = sys.stdin.readline

    from math import isqrt

    def A123663(n):
        return (m := n << 1) - 1 - isqrt((m << 1) - 1)

    for _ in range(int(input())):
        n = int(input())
        print(A123663(n))


if __name__ == "__main__":
    main()
