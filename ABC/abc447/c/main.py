import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    t = input()

    if s.replace("A", "") != t.replace("A", ""):
        print(-1)
        return

    ss = []
    cnt = 0
    for S in s:
        if S == "A":
            cnt += 1
        else:
            ss.append(cnt)
            cnt = 0
    ss.append(cnt)

    tt = []
    cnt = 0
    for T in t:
        if T == "A":
            cnt += 1
        else:
            tt.append(cnt)
            cnt = 0
    tt.append(cnt)

    ans = 0
    for i in range(len(ss)):
        ans += abs(ss[i] - tt[i])

    print(ans)


if __name__ == "__main__":
    main()
