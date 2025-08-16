import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    
    s = input()
    ans = defaultdict(lambda: "Unknown")
    ans["red"] = "SSS"
    ans ["blue"] = "FFF"
    ans["green"] = "MMM"
    print(ans[s])


if __name__ == '__main__':
    main()
