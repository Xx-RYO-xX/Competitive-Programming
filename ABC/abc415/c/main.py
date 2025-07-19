import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import deque
    for _ in range(int(input())):
        n = int(input())
        s = input()
        
        n_bit = (1<<n)-1        
        d = set()
        for i in range(len(s)):
            if s[i] == '1':
                d.add(i+1)
        
        visited = {0}
        q = deque([0])
        while q:
            joutai = q.popleft()
            if joutai == n_bit:
                print("Yes")
                break
            for i in range(n):
                if not (joutai & (1<<i)):
                    n_joutai = joutai | (1<<i)
                    if n_joutai not in d and n_joutai not in visited:
                        visited.add(n_joutai)
                        q.append(n_joutai)
        else:
            print("No")


if __name__ == '__main__':
    main()
