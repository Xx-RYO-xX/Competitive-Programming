def main():
    import sys

    input = sys.stdin.readline
    
    n = int(input())
    s = input()[:-1]

    stuck = []
    ans = 0
    for S in s:
        if S == "S":
            ans = max(ans, len(stuck))
            stuck = []
        else:
            stuck.append(S)
    print(max(ans, len(stuck)))

if __name__ == "__main__":
    main()
