import sys


def input(): return sys.stdin.readline().rstrip()


def main():
    k = int(input())
    s = input()
    t = input()
    
    if s == t:
        print("Yes")
        return

    len_s, len_t = len(s), len(t)

    if len_s == len_t+1:
        j = 0
        for i in range(len_s):
            if j < len_t and s[i] == t[j]:
                j += 1
            elif j == len_t:
                print("Yes")
                return
        if j == len_t:
            print("Yes")
            return

    elif len_s+1 == len_t:
        j = 0
        for i in range(len_t):
            if j < len_s and t[i] == s[j]:
                j += 1
            elif j == len_s:
                print("Yes")
                return
        if j == len_s:
            print("Yes")
            return

    elif len_s == len_t:
        diff_count = 0
        for i in range(len_s):
            if s[i] != t[i]:
                diff_count += 1
                if diff_count > 1:
                    print("No")
                    return
        if diff_count == 1:
            print("Yes")
            return

    print("No")


if __name__ == '__main__':
    sys.exit(main())
