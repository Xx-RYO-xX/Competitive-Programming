def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    a100, a10, a1 = 0, 0, 0
    for A in a:
        oturi = A//1000 
        a100 += A//100
        oturi = A//100
        a10 += A//10
        oturi = A//10
        a1+= oturi

    print(a1, a10, a100)

if __name__ == "__main__":
    main()
