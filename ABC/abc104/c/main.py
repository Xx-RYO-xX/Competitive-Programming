import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations

    d, g = map(int, input().split())
    ipc = []
    for i in range(1, d + 1):
        p, c = map(int, input().split())
        ipc.append((100 * i, p, c))

    ans = float("inf")
    for perm in permutations(ipc):
        anst = 0
        point = 0
        for i, p, c in perm:
            for j in range(p):
                point += i
                anst += 1
                if g <= point:
                    ans = min(ans, anst)
                    break
            else:
                point += c
                if g <= point:
                    ans = min(ans, anst)
                    break
                continue
            break
    print(ans)


if __name__ == "__main__":
    main()
