def main():
    a, b, c, d = map(int, input().split())
    
    ans = 0
    while True:
        if a == 0 and 0 < d:
            a += 1
            d -= 1
        if b == 0 and 0 < d:
            b += 1
            d -= 1
        if c == 0 and 0 < d:
            c += 1
            d -= 1
        if 0 < a and 0 < b and 0 < c:
            ans += 1
            a -= 1
            b -= 1
            c -= 1
        else:
            print(ans)
            exit()

if __name__ == '__main__':
    main()