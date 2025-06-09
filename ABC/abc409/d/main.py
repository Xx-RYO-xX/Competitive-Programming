import sys


def input(): return sys.stdin.readline().rstrip()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        l = next((i for i in range(n-1) if s[i] > s[i+1]), None)
        if l is None:
            print(s)
            continue


        def char_at(r, pos):
            if pos < l:
                return s[pos]
            elif pos <= r-1:
                return s[pos+1]
            elif pos == r:
                return s[l]
            else:
                return s[pos]

        best_r = l+1
        for r in range(l+2, n):
            for t in range(l, n):
                cj = char_at(r, t)
                cb = char_at(best_r, t)
                if cj == cb:
                    continue
                if cj < cb:
                    best_r = r
                break

        r = best_r
        ans = s[:l]+s[l+1:r+1]+s[l]+s[r+1:]
        print(ans)

if __name__ == '__main__':
    main()
