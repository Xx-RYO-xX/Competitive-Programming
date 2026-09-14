def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    w = []
    taka = 0
    ao = 0
    for i in range(n):
        if a[i] <= b[i]:
            w.append(1)
        elif a[i] > b[i]:
            w.append(10**18)

        taka += a[i] * w[-1]
        ao += b[i] * w[-1]
    if taka > ao:
        print("Yes")
        print(*w)
    else:
        print("No")


if __name__ == "__main__":
    main()
