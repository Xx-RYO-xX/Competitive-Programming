import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, a, b = map(int, input().split())
    d = sorted(set(map(lambda x: int(x) % (a + b), input().split())))

    print(
        "Yes"
        if max(d) - min(d) < a
        or any((d[(i + 1) % len(d)] - d[i]) % (a + b) > b for i in range(len(d)))
        else "No"
    )


if __name__ == "__main__":
    main()
