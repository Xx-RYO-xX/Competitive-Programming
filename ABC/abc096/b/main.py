import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    abc = list(map(int, input().split()))
    k = int(input())
    abc.append((2**k) * (abc.pop(abc.index(max(abc)))))
    print(sum(abc))


if __name__ == "__main__":
    main()
