def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    q1_plus = 0
    q2_plus = [0]*n
    for _ in range(q):
        query = input()
        if query[0] == "1":
            que, x = map(int, query.split())
            q1_plus += x
        
        if query[0] == "2":
            que, i, x = map(int, query.split())
            q2_plus[i-1] += x
        
        if query[0] == "3":
            que, i = map(int, query.split())
            print(a[i-1] + q1_plus + q2_plus[i-1])
    
if __name__ == '__main__':
    main()