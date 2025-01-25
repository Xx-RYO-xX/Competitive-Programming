import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    w = input()
    last_word = w[-1]
    say = set()
    say.add(w)
    for i in range(n-1):
        w = input()
        if w not in say and last_word == w[0]:
            say.add(w)
            last_word = w[-1]
        else:
            if i % 2 == 0:
                print("WIN")
            else:
                print("LOSE")
            return
    
    print("DRAW")

if __name__ == '__main__':
    sys.exit(main())
