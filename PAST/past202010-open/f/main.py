import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict, Counter
    
    n, k = map(int, input().split())
    s = defaultdict(int)
    for _ in range(n):
        s[input()] += 1
    
    word = sorted(s.items(), key=lambda x:x[1], reverse=True)
    value_cnt = Counter(s.values())
    
    if value_cnt[word[k-1][1]] == 1:
        print(word[k-1][0])
    else:
        print("AMBIGUOUS")



if __name__ == '__main__':
    main()
