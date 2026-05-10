import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    s = []
    out = set()
    for _ in range(n):
        st = list(input())
        outt = ""
        for stt in st:
            if stt == "0":
                outt += "1"
            else:
                outt += "0"
        out.add(outt)

    for i in range(n + 1):
        moji = bin(i)[2:].zfill(m)
        if moji not in out and len(moji) == m:
            print("Yes")
            print(moji)
            return
    print("No")


if __name__ == "__main__":
    main()
