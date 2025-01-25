import sys


def input():return sys.stdin.readline().rstrip()


def main():
    MOD = 998244353
    from collections import deque 
    q = int(input())
    s = 1
    s_str = deque([1])
    for _ in range(q):
        query = input()
        if query[0] == "1":
            Q, x =  map(int, query.split())
            s *= 10
            s += x
            s_str.append(x)
        if query[0] == "2":
            sentou = int(s_str.popleft())
            minus = sentou * 10**len(s_str)
            # print(sentou, minus)
            s -= minus
        
        if query[0] == "3":
        # print(s_str)
            print(s%MOD)


if __name__ == '__main__':
    main()
