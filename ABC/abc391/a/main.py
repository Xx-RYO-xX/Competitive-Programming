import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    d = input()
    ans = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E',
        'NE': 'SW',
        'NW': 'SE',
        'SE': 'NW',
        'SW': 'NE'
    }
    print(ans[d])

if __name__ == '__main__':
    sys.exit(main())
