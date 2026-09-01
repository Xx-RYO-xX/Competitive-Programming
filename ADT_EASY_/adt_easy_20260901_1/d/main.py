def main():
    import sys

    input = sys.stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    
    if s == t:
        print(0)
        return
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(min(len(s), len(t))+1)

if __name__ == "__main__":
    main()
