import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()

    s_len = len(s)
    ans = 0
    for i in range(s_len):
        for j in range(i+1, s_len):
            for k in range(j+1, s_len):
                if j-i == k-j and s[i] == "A" and s[j] == "B" and s[k] == "C":
                    ans += 1
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
