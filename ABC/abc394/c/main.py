import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()

    n = len(s)
    ans = []
    i = 0
    while i < n:
        if s[i] == 'W':
            start = i
            while i < n and s[i] == 'W':
                i += 1
            count_w = i-start

            if i < n and s[i] == 'A':
                ans.append('A'+'C'*count_w)
                i += 1  
            else:
                ans.append('W'*count_w)
        else:
            ans.append(s[i])
            i += 1

    print("".join(ans))


if __name__ == '__main__':
    sys.exit(main())
