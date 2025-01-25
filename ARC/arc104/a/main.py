import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    for x in range(-1000, 1000):
        for y in range(-1000, 1000):
            if x+y == a and x-y == b:
                print(x, y)
                exit()

if __name__ == "__main__":
    main()
