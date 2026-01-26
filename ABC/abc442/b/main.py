import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    q = int(input())
    vol = 0
    is_stop = 1
    for _ in range(q):
        a = int(input())
        match a:
            case 1:
                vol += 1
            case 2:
                if vol >= 1:
                    vol -= 1
            case 3:
                is_stop *= -1

        if vol >= 3 and is_stop == -1:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
