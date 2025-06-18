import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c, d = list(input())
    
    kigou = ["+", "-"]
    
    for op1 in kigou:
        for op2 in kigou:
            for op3 in kigou:
                siki = a+op1+b+op2+c+op3+d
                if eval(siki)==7:
                    print(siki+"=7")
                    return


if __name__ == '__main__':
    sys.exit(main())
