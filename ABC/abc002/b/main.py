import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    w = input()
    ans = ""
    for W in w:
        if W not in "aiueo":
            ans += W
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
