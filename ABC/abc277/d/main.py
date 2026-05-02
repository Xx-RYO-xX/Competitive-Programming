import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))

    aa = a + a

    seq = []
    seqt = [0]
    for i in range(2 * n - 1):
        if aa[i] == aa[i + 1] or (aa[i] + 1) % m == aa[i + 1]:
            seqt.append(i + 1)
        else:
            seq.append(seqt)
            seqt = [i + 1]
    if seqt:
        seq.append(seqt)

    # print(aa)
    # print(seq)

    ans = float("inf")
    suma = sum(a)
    for seqt in seq:
        sums = 0
        for i in seqt:
            sums += aa[i]
        # print(sums)
        ans = min(ans, suma - sums if suma - sums > 0 else 0)

    print(ans)


if __name__ == "__main__":
    main()
