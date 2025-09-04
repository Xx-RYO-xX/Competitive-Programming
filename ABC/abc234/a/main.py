import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    t = int(input())

    def f(x):
        return x**2 + 2 * x + 3

    print(f(f(f(t) + t) + f(f(t))))


if __name__ == "__main__":
    main()
