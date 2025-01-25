import sys


def input(): return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    xor = set()
    sys.setrecursionlimit(10**9)
    
    
    def dfs(stone, visited):
        state = tuple(stone)
        if state in visited:
            return
        
        visited.add(state)
        
        current_xor = 0
        for x in stone:
            current_xor ^= x
        xor.add(current_xor)
        
        for i in range(n):
            for j in range(n):
                if i != j and stone[i] > 0:
                    new_stone = list(stone)
                    new_stone[j] += new_stone[i]
                    new_stone[i] = 0
                    dfs(new_stone, visited)
    
    visited = set()
    dfs(a, visited)
    print(len(xor))


if __name__ == '__main__':
    sys.exit(main())