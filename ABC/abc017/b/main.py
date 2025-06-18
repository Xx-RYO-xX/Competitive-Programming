import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    x = input()
    choku = {"", "c", "h", "o", "k", "u"}
    for i in range(len(x)):
        if x[i] not in choku:
            print("NO")
            return
    oku = {"o", "k", "u"}
    for i in range(len(x)-1):
        if x[i] == "c":
            if x[i+1] == "h":
                continue
            else:
                print("NO")
                return
        if x[i] == "h":
            if x[i+1] in oku:
                continue
            else:
                print("NO")
                return
    
    print("YES")

if __name__ == '__main__':
    sys.exit(main())
