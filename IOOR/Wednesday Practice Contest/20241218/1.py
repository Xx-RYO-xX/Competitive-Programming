def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    cond = True
    for A in a:
        if A % 2 == 0:
            if A % 3 == 0 or A % 5 == 0:
                continue
            else:
                cond = False
                break
    
    print("APPROVED" if cond else "DENIED")

if __name__ == '__main__':
    main()