import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    import heapq

    for _ in range(int(input())):
        s = Counter(input()).items()
        ss = []
        for chr, cnt in s:
            ss.append([-1 * cnt, chr])
        heapq.heapify(ss)
        # print(ss)

        ans = []
        while ss:
            cnt, chr = heapq.heappop(ss)
            if not ans or ans[-1] != chr:
                ans.append(chr)
                cnt += 1
            else:
                if not ss:
                    break
                cnt2, chr2 = heapq.heappop(ss)
                heapq.heappush(ss, [cnt, chr])
                cnt, chr = cnt2, chr2
                ans.append(chr)
                cnt += 1

            if cnt != 0:
                heapq.heappush(ss, [cnt, chr])
        else:
            print("Yes")
            print(*ans, sep="")
            continue
        print("No")


if __name__ == "__main__":
    main()
