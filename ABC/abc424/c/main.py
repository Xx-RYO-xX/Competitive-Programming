import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict, deque

    n = int(input())
    abi = []
    skil = [False] * (n + 1)
    skil_to_able = defaultdict(set)
    q = deque()
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        if a == b == 0:
            skil[i] = True
            q.append(i)

        abi.append((a, b, i))
        skil_to_able[a].add(i)
        skil_to_able[b].add(i)

    # print(q)
    # print(skil_to_able)
    while q:
        num = q.popleft()
        for skil_num in skil_to_able[num]:
            if not skil[skil_num]:
                skil[skil_num] = True
                q.append(skil_num)

    print(sum(skil))


if __name__ == "__main__":
    main()
