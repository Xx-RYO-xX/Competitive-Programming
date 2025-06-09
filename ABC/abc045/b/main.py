import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = dict()
    s["a"]=list(input())
    s['b']=list(input())
    s['c']=list(input())
    turn = "a"
    while True:
        if len(s[turn]) == 0:
            print(turn.upper())
            return
        suteru =  s[turn].pop(0)
        turn = suteru



if __name__ == '__main__':
    sys.exit(main())
