def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    s = list(input())[:-1]
    t = list(input())[:-1]

    for i in range(n):
        if s[i] != t[i] and t[i] != "*":
            print("No")
            return
    print("Yes")

if __name__ == "__main__":
    main()
