def main():
    from itertools import accumulate
    n = int(input())
    a = list(map(int, input().split()))
    
    accm = list(accumulate(a, lambda x, y: x-y))
    
    print(accm)


if __name__ == '__main__':
    main()