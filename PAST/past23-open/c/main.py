def main():
    import sys

    input = sys.stdin.readline
    n, k = map(int, input().split())
    s = list(input())

    for i in range(k ,n):
        if s[i]=="o":
            print(i+1)
            return

if __name__ == "__main__":
    main()
