import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    ans = {"ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"}
    print("Yes" if s in ans else "No")


if __name__ == "__main__":
    main()
