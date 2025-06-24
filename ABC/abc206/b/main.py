import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    
    i = 1
    chokin = 0
    while True:
        chokin += i
        if n <= chokin:
            print(i)
            return
        i += 1


if __name__ == '__main__':
    main()
