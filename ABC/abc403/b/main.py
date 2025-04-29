import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    t = input()
    u = input()
    
    for one in "abcdefghijklmnopqrstuvwxyz":
        for two in "abcdefghijklmnopqrstuvwxyz":
            for three in "abcdefghijklmnopqrstuvwxyz":
                for four in "abcdefghijklmnopqrstuvwxyz":
                    tt = list(t)
                    count = 0
                    for i in range(len(t)):
                        if tt[i] == "?":
                            if count == 0:
                                tt[i] = one
                                count += 1
                            elif count == 1:
                                tt[i] = two
                                count += 1
                            elif count == 2:
                                tt[i] = three
                                count += 1
                            elif count == 3:
                                tt[i] = four
                                count += 1
                    if u in "".join(tt):
                        print("Yes")
                        return
    print("No")
    


if __name__ == '__main__':
    sys.exit(main())
