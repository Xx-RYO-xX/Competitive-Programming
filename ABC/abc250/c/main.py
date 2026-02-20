import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    a = [i for i in range(1, n + 1)]
    num_to_idx = dict()
    for idx, num in enumerate(a):
        num_to_idx[num] = idx

    for _ in range(q):
        x = int(input())
        left_num = x if num_to_idx[x] != n - 1 else a[-2]
        right_num = a[num_to_idx[x] + 1] if num_to_idx[x] != n - 1 else a[-1]

        left_idx = num_to_idx[left_num]
        right_idx = left_idx + 1

        a[left_idx], a[right_idx] = a[right_idx], a[left_idx]

        num_to_idx[left_num] = right_idx
        num_to_idx[right_num] = left_idx

    print(*a)


if __name__ == "__main__":
    main()
