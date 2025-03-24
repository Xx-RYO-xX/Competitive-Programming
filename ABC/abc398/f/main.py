import sys


def input(): return sys.stdin.readline().rstrip()


def make_kmp_table(t):
    i = 2
    j = 0
    m = len(t)
    tbl = [0]*(m+1)
    tbl[0] = -1
    while i <= m:
        if t[i-1] == t[j]:
            tbl[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = tbl[j]
        else:
            tbl[i] = 0
            i += 1
    return tbl


def kmp(s, t):
    matched_indices = []
    tbl = make_kmp_table(t)
    i = 0
    j = 0
    n = len(s)
    m = len(t)
    while i + j < n:
        if t[j] == s[i + j]:
            j += 1
            if j == m:
                matched_indices.append(i)
                i += j - tbl[j]
                j = tbl[j]
        else:
            i += j - tbl[j]
            if j > 0:
                j = tbl[j]
    return matched_indices


def main():
    s = input()
    
    t =  s[::-1]+'#'+s
    mkt = make_kmp_table(t)
    k = mkt[len(t)]  

    ans = s+s[::-1][k:]

    print(ans)

if __name__ == '__main__':
    sys.exit(main())
