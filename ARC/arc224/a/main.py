def main():
    import sys

    input = sys.stdin.readline

    for _ in range(int(input())):
        k = int(input())
        for i in range(1000):
            n = k * i
            nn = str(n)
            if "00" in nn:
                print(n)
                break


if __name__ == "__main__":
    main()
