import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    def f(num):
        nums = list(map(int, list(str(num))))
        return sum(nums)

    ans = []
    for i in range(n + 1):
        if i == 0:
            ans.append(1)
        else:
            ans.append(ans[-1] + f(ans[-1]))

    print(ans[n - 1])


if __name__ == "__main__":
    main()
