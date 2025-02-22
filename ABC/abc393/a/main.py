import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s1, s2 = input().split()

    if s1 == "sick" and s2 == "sick":
        print(1)
    elif s1 == "sick":
        print(2)
    elif s2 == "sick":
        print(3)
    else:
        print(4)


if __name__ == '__main__':
    sys.exit(main())
