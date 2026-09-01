def main():
    import sys

    input = sys.stdin.readline
    s = input()[:-1]
    t = input()[:-1]

    if len(s) > len(t):
        print("No")
        return
    
    if s == t[:len(s)]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
