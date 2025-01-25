import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import deque
    q = int(input())
    snake = deque()
    minus = 0
    for _ in range(q):
        query = input()
        if query[0] == "1":
            num, l = map(int, query.split())
            if len(snake) == 0:
                snake.append(l)
            else:
                snake.append(snake[-1]+l)
        elif query[0] == "2":
            minus = snake.popleft()
        else:
            num, k = map(int, query.split())
            if k == 1:
                print(0)
            else:
                print(snake[k-2]-minus)
        # print(snake)

if __name__ == '__main__':
    sys.exit(main())
