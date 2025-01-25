import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a = list(map(int, input().split()))
    b = sorted(a)
    if a == b:
        print("No")
        return

    
    for i in range(4):
        a_copy = a[:]
        a_copy[i], a_copy[i+1] = a_copy[i+1], a_copy[i]
        if a_copy == b:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    sys.exit(main())
