import sys


def input():
    return sys.stdin.readline().rstrip()


def main():

    a, b = map(int, input().split())

    ans = 0
    flagAce = False
    for num in [a, b]:
        if num == 1:
            flagAce = True
            ans += 1
        if 11 <= num <= 13:
            ans += 10
        if 2 <= num <= 10:
            ans += num

    if flagAce and ans <= 11:
        ans += 10

    print("BLACJACK" if ans == 21 else ans)


if __name__ == "__main__":
    main()
