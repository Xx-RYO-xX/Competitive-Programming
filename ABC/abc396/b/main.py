import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    q = int(input())
    card = [0]*100
    for _ in range(q):
        query = input()
        if query[0] == "1":
            t, x = map(int, query.split())
            card.append(x)
        else:
            print(card.pop(-1))


if __name__ == '__main__':
    sys.exit(main())
