import sys


def input():return sys.stdin.readline().rstrip()


class Train():
    def __init__(self):
        self.before = 0
        self.after = 0
    
    def is_sentou(self):
        return self.before == 0
    
    def is_usiro(self):
        return self.after == 0
    
    def __str__(self):
        return '(before:{0}, after:{1})'.format(self.before, self.after)
    def __repr__(self):
        return str(self)


def main():
    n, q = map(int, input().split())
    train = [Train() for _ in range(n+1)]
    for _ in range(q):
        query = input()
        if query[0]=="1":
            num, x, y = map(int, query.split())
            train[x].after = y
            train[y].before = x
        elif query[0]=="2":
            num, x, y = map(int, query.split())
            train[x].after = 0
            train[y].before = 0
        else:
            num, x = map(int, query.split())

            ans = []
            if not train[x].is_sentou():
                bidx = train[x].before
                bans = [bidx]
                while not train[bidx].is_sentou():
                    bidx = train[bidx].before
                    bans.append(bidx)

                for i in range(len(bans))[::-1]:
                    ans.append(bans[i])

            ans.append(x)

            if not train[x].is_usiro():
                aidx = train[x].after
                ans.append(aidx)
                while not train[aidx].is_usiro():
                    aidx = train[aidx].after
                    ans.append(aidx)
                

            print(len(ans), *ans)


if __name__ == '__main__':
    main()
