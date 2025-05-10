import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import deque
    s = deque(list(input()))
    is_reversed = 1
    q = int(input())
    for _ in range(q):
        query = input()
        
        if query[0] == "1":
            is_reversed *= -1
        else:
            t, f, c = query.split()
            if f == "2": f = -1
            f = int(f)*is_reversed
            if f == 1:
                s.appendleft(c)
            else:
                s.append(c)
    
    if is_reversed == 1:
        print(*s, sep="")
    else:
        print("".join(s)[::-1])


if __name__ == '__main__':
    sys.exit(main())
