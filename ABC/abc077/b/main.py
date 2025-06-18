import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    print(int(int(input())**(1/2))**2)


if __name__ == '__main__':
    sys.exit(main())
