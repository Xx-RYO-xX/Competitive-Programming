import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    q = int(input())
    seiseki = dict()
    for _ in range(q):
        query = input()
        if query[0] == "1":
            num, x, y = query.split()
            seiseki[x] = y
        else:
            num, x = query.split()
            print(seiseki[x])


if __name__ == '__main__':
    main()
