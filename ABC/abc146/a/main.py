import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    week = {"SUN": 7, "MON": 6, "TUE": 5, "WED": 4, "THU": 3, "FRI": 2, "SAT": 1}

    print(week[s])


if __name__ == "__main__":
    main()
