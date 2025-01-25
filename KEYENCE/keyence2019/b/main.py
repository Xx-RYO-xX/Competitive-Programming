import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    S = input()
    key = "keyence"
    n = len(S)
    k = len(key)
    for i in range(n - k +1):
        if S[i:i+k] == key:
            print("YES")
            return
    for i in range(k+1):
        if S[:i] == key[:i] and S[-(k-i):] == key[i:]:
            print("YES")
            return
    print("NO")


if __name__ == '__main__':
    main()
