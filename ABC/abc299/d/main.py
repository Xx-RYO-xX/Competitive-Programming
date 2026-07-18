import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    ok = 1
    ng = n
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        print("? " + str(mid), flush=True)
        res = int(input())
        if res == 0:
            ok = mid
        else:
            ng = mid

    print("! " + str(ok), flush=True)


if __name__ == "__main__":
    main()
