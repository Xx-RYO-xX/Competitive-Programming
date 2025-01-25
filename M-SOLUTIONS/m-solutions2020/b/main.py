import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c = map(int, input().split())
    k = int(input())
    
    card = {"R":a, "G":b, "B":c}
    
    tmp = sorted(card.items(), key=lambda x: x[1])
    
    print(tmp)



if __name__ == '__main__':
    main()
