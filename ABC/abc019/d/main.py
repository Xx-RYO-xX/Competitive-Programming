import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    u = 0
    max_dist = 0
    for i in range(2, n + 1):
        print("? 1 " + str(i), flush=True)
        dist = int(input())
        if max_dist < dist:
            max_dist = dist
            u = i

    max_dist = 0
    for i in range(1, n + 1):
        if i == u:
            continue
        print("? " + str(u) + " " + str(i), flush=True)
        dist = int(input())
        if max_dist < dist:
            max_dist = dist

    print("! " + str(max_dist), flush=True)


if __name__ == "__main__":
    main()
