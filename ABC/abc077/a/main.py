import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import numpy as np
    c = []
    for _ in  range(2):
        c.append(list(input()))
    
    c = np.array(c)
    if np.array_equal(c, np.rot90(c, 2)):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    sys.exit(main())
