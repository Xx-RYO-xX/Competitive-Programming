import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    hw = list(map(int, input().split()))
    h = hw[:3]
    w = hw[3:]
    count = 0
    for a in range(1, h[0]):
        for b in range(1, h[0] - a):
            c = h[0] - a - b
            for d in range(1, h[1]):
                for e in range(1, h[1] - d):
                    f = h[1] - d - e
                    for g in range(1, h[2]):
                        for h_val in range(1, h[2] - g):
                            i = h[2] - g - h_val
                            if a + d + g == w[0] and b + e + h_val == w[1] and c + f + i == w[2]:
                                count += 1
    print(count)


if __name__ == '__main__':
    sys.exit(main())
