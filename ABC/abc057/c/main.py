import sys


def input():
    return sys.stdin.readline().rstrip()


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            for _ in range(cnt):
                arr.append(i)

    if temp != 1:
        arr.append(temp)

    if arr == []:
        arr.append(n)

    return arr


def main():
    from itertools import combinations

    n = int(input())
    arr = factorization(n)

    def f(a=1, b=1):
        return max(len(str(a)), len(str(b)))

    # print(arr)
    lens = len(arr)
    ans = float("inf")
    for i in range(2**lens):
        a = 1
        b = 1
        for j in range(lens):
            bit = 2**j
            if (i // bit) % 2 == 1:
                a *= arr[j]
            else:
                b *= arr[j]
        ans = min(ans, f(a, b))

    print(ans)


if __name__ == "__main__":
    main()
