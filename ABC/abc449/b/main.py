import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w, q = map(int, input().split())
    ita = [[True] * w for _ in range(h)]
    for _ in range(q):
        num, rc = map(int, input().split())
        if num == 1:
            cnt = 0
            eat = 0
            for i in range(h - 1, -1, -1):
                if ita[i][0] == True:
                    for j in range(w):
                        if ita[i][j]:
                            cnt += 1
                            ita[i][j] = False
                    eat += 1
                if eat == rc:
                    break
            print(cnt)
        else:
            cnt = 0
            eat = 0
            for j in range(w - 1, -1, -1):
                if ita[0][j] == True:
                    for i in range(h):
                        if ita[i][j]:
                            cnt += 1
                            ita[i][j] = False
                    eat += 1
                if eat == rc:
                    break
            print(cnt)


if __name__ == "__main__":
    main()
