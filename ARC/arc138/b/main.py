def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(lambda x: int(-1) if x == "0" else int(1), input().split()))

    from collections import deque

    a = deque(a)
    flip = 1
    while a:
        if a[-1] * flip == -1:
            a.pop()
        elif a[0] * flip == -1:
            a.popleft()
            flip *= -1
        else:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
