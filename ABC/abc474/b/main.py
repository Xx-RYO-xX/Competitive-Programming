def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    p = list(map(int, input().split()))

    for i in range(n):
        if 1+10*(i//10) <= p[i] <= 10+10*(i//10):
            None
        else:
            print("No")
            return
    print("Yes")

if __name__ == "__main__":
    main()
