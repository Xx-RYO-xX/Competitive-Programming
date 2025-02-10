import sys


def input(): return sys.stdin.readline().rstrip()


def main():
    from collections import Counter

    n = int(input())
    k = []
    saikoro = []
    for _ in range(n):
        ka = list(map(int, input().split()))
        k.append(ka[0])
        saikoro.append(ka[1:])
    
    ans = 0.0

    for i in range(n):
        for j in range(i+1, n):
            counter_i = Counter(saikoro[i])
            counter_j = Counter(saikoro[j])
            total_i = k[i]
            total_j = k[j]
            
            face_num = set(counter_i.keys()) & set(counter_j.keys())
            kakuritu = sum((counter_i[face] / total_i) * (counter_j[face] / total_j) for face in face_num)
            
            ans = max(ans, kakuritu)
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())