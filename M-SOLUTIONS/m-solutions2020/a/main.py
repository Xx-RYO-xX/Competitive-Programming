import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    x = int(input())
    
    if 400 <= x <= 599:
        print("8")
    elif 600 <= x <= 799:
        print("7")
    elif 800 <= x <= 999:
        print("6")
    elif 1000 <= x <= 1199:
        print("5")
    elif 1200 <= x <= 1399:
        print("4")
    elif 1400 <= x <= 1599:
        print("3")
    elif 1600 <= x <= 1799:
        print("2")
    elif 1800 <= x <= 1999:
        print("1")


if __name__ == '__main__':
    main()
