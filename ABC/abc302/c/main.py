def is_diff(s1, s2, m):
    count = 0
    for i in range(m):
        if s1[i] != s2[i]:
            count += 1
    
    return count == 1


def main():
    from itertools import permutations

    n, m = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())
    idx_lst = list(permutations(range(n), n))
    
    for lst in idx_lst:
        for i in range(n-1):
            if not is_diff(s[lst[i]], s[lst[i+1]], m):
                break
        else:
            print("Yes")
            exit()
    
    print("No")

if __name__ == '__main__':
    main()