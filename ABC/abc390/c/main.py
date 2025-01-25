import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    s = []
    black_masu = []
    for i in range(h):
        row = input()
        s.append(row)
        for j in range(w):
            if row[j] == '#':
                black_masu.append((i, j))


    min_i = min(i for i, _ in black_masu)
    max_i = max(i for i, _ in black_masu)
    min_j = min(j for _, j in black_masu)
    max_j = max(j for _, j in black_masu)

    for i in range(h):
        for j in range(w):
            if min_i <= i <= max_i and min_j <= j <= max_j:
                if s[i][j] == '.':
                    print("No")
                    return
            else:
                if s[i][j] == '#':
                    print("No")
                    return
    
    print("Yes")


if __name__ == '__main__':
    sys.exit(main())
