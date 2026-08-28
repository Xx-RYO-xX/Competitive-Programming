def main():
    import sys

    input = sys.stdin.readline
    a, b, c = map(int, input().split())
    if a+c==b:
        print(*[a, " ","->", " ",  b," ", "(", c if c < 0 else "+"+str(c), ")" ], sep="")
    else:
        print(*[b, " ","->", " ",  a," ", "(", c if c < 0 else "+"+str(c), ")" ], sep="")

if __name__ == "__main__":
    main()
