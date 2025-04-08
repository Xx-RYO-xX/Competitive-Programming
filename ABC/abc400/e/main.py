import sys, math, bisect

def input():
    return sys.stdin.readline().rstrip()



def main():

    max_s = 10**6
    spf = list(range(max_s+1))
    for i in range(2, int(math.sqrt(max_s)) + 1):
        if spf[i] == i:
            for j in range(i*i, max_s+1, i):
                if spf[j] == j:
                    spf[j] = i

    semiprime_list = []
    for num in range(6, max_s+1):
        distinct = set()
        temp = num
        while temp > 1:
            distinct.add(spf[temp])
            temp //= spf[temp]
            if len(distinct) > 2:
                break
        if len(distinct) == 2:
            semiprime_list.append(num)

    numbers = [s * s for s in semiprime_list if s * s <= 10**12]
    numbers.sort()

    q = int(input())
    for _ in range(q):
        a = int(input())
        idx = bisect.bisect_right(numbers, a) - 1
        print(numbers[idx])


if __name__ == '__main__':
    sys.exit(main())