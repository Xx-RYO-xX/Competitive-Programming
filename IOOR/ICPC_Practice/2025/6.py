import sys


def input():return sys.stdin.readline().rstrip()


def main():
    while True:
        n = int(input())
        if n == 0: return
        s = list(input())
        suponser = []
        for i in range(1, n):
            if s[i] == "o":
                suponser.append(i)
        print(suponser)


if __name__ == '__main__':
    main()
