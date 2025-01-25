def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    last_set = None
    added = {}
    
    for _ in range(q):
        query = input()
        parts = query.split()
        if parts[0] == "1":
            x = int(parts[1])
            last_set = x
            added = {}
        elif parts[0] == "2":
            i = int(parts[1]) - 1
            x = int(parts[2])
            if last_set is not None:
                if i in added:
                    added[i] += x
                else:
                    added[i] = x
            else:
                a[i] += x
        elif parts[0] == "3":
            i = int(parts[1]) - 1
            if last_set is not None:
                print(last_set + added.get(i, 0))
            else:
                print(a[i])

if __name__ == '__main__':
    main()