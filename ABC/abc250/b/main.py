import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, a, b = map(int, input().split())
    one = ""
    for i in range(n):
        if i % 2 == 0:
            one += "." * b
        else:
            one += "#" * b
    two = ""
    for i in range(n):
        if i % 2 == 0:
            two += "#" * b
        else:
            two += "." * b

    for i in range(a * n):
        if (i // a) % 2 == 0:
            print(one)
        else:
            print(two)


if __name__ == "__main__":
    main()
