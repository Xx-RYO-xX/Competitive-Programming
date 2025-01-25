import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    pair = []
    for i in range(n):
        pair.append((a[i], i))
    
    pair.sort()
    
    b = [0]*n
    count= 1
    for i in range(n):
        aa, ii = pair[i]
        b[ii] = count
        if i != 0 and pair[i-1][0] == aa:
            b[ii] -= 1
            continue
        else:
            count += 1
    
    print(*b)


if __name__ == '__main__':
    main()
