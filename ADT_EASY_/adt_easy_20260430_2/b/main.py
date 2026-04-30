import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m, x, t, d = map(int, input().split())

    age = [t]
    for i in range(x):
        age.append(age[-1] - d)
    age = age[::-1]

    # print(age, len(age))
    if m <= x:
        print(age[m])
    else:
        print(t)


if __name__ == "__main__":
    main()
