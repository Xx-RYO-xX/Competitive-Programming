import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-(n**0.5) // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                    arr.append(i)

        if temp != 1:
            arr.append(temp)

        if arr == []:
            arr.append(n)

        return arr

    n = int(input())

    print(*factorization(n))


if __name__ == "__main__":
    main()
