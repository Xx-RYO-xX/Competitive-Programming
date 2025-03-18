import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    
    p = list(map(int, input().split()))
    ko_to_oya = dict()
    for i in range(n-1):
        oya, ko = p[i], i+2
        ko_to_oya[ko] = oya
    
    c = list(map(int, input().split()))
    num_to_youryou = dict()
    num_to_youryou[1] = float("inf")
    for i in range(n-1):
        num_to_youryou[i+2] = c[i]
    
    a = list(map(int, input().split()))
    num_to_hokan = dict()
    num_to_hokan[1] = float("inf")
    for i in range(n-1):
        num_to_hokan[i+2] = a[i]
    
    # print(ko_to_oya)
    # print(num_to_youryou)
    # print(num_to_hokan)
    
    # print(list(num_to_youryou[i] for i in range(2, n+1)))
    # print(list(num_to_hokan[i] for i in range(2, n+1)))
    
    q = int(input())
    for _ in range(q):
        query = input()
        
        if query[0] == "1":
            __, v, x = map(int, query.split())
    
            num_to_hokan[v] -= x

            oya, ko = ko_to_oya[v], v
            while num_to_hokan[ko] < 0:
                husoku = abs(num_to_hokan[ko])
                num_to_hokan[oya] -= husoku
                num_to_hokan[ko] = 0
                if oya == 1:break
                oya, ko = ko_to_oya[oya], oya
        
        elif query[0] == "2":
            __, v, x = map(int, query.split())
        
            num_to_hokan[v] += x
            
            oya, ko = ko_to_oya[v], v
            while num_to_hokan[ko] > num_to_youryou[ko]:
                over = num_to_hokan[ko] - num_to_youryou[ko]
                num_to_hokan[oya] += over
                num_to_hokan[ko] -= over
                if oya == 1:break
                oya, ko = ko_to_oya[oya], oya

        
        else:
            __, v = map(int, query.split())
            print(num_to_hokan[v])
        
        # print(list(num_to_youryou[i] for i in range(2, n+1)))
        # print(list(num_to_hokan[i] for i in range(2, n+1)))


if __name__ == '__main__':
    main()
