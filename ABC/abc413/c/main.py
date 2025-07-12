import sys


def input():return sys.stdin.readline().rstrip()

class Deque:
    """
    O(1)でランダムアクセスできるdeque
    """

    def __init__(self, src_arr=[], max_len=300000):
        self.N = max(max_len, len(src_arr)) + 1
        self.buf = list(src_arr) + [None] * (self.N - len(src_arr))
        self.head = 0
        self.tail = len(src_arr)

    def __index(self, i):
        l = len(self)
        if not -l <= i < l: raise IndexError('index out of range: ' + str(i))
        if i < 0:
            i += l
        return (self.head + i) % self.N

    def __extend(self):
        ex = self.N - 1
        self.buf[self.tail + 1: self.tail + 1] = [None] * ex
        self.N = len(self.buf)
        if self.head > 0:
            self.head += ex

    def is_full(self):
        return len(self) >= self.N - 1

    def is_empty(self):
        return len(self) == 0

    def append(self, x):
        if self.is_full(): self.__extend()
        self.buf[self.tail] = x
        self.tail += 1
        self.tail %= self.N

    def appendleft(self, x):
        if self.is_full(): self.__extend()
        self.buf[(self.head - 1) % self.N] = x
        self.head -= 1
        self.head %= self.N

    def pop(self):
        if self.is_empty(): raise IndexError('pop() when buffer is empty')
        ret = self.buf[(self.tail - 1) % self.N]
        self.tail -= 1
        self.tail %= self.N
        return ret

    def popleft(self):
        if self.is_empty(): raise IndexError('popleft() when buffer is empty')
        ret = self.buf[self.head]
        self.head += 1
        self.head %= self.N
        return ret

    def rotate(self, n=1):
        if n > 0:
            for _ in range(n):
                self.appendleft(self.pop())
        else:
            for _ in range(abs(n)):
                self.append(self.popleft())

    def __len__(self):
        return (self.tail - self.head) % self.N

    def __getitem__(self, key):
        return self.buf[self.__index(key)]

    def __setitem__(self, key, value):
        self.buf[self.__index(key)] = value

    def __str__(self):
        return 'Deque({0})'.format(str(list(self)))



def main():
    q = int(input())
    a = Deque()
    
    for _ in range(q):
        query = input()
        if query[0] == "1":
            num, c, x = map(int, query.split())
            if a and a[-1][0] == x:
                a[-1] = (x, a[-1][1]+c)
            else:
                a.append((x, c))
        
        else:
            num, k = map(int, query.split())
            ans = 0
            
            while k > 0 and a:
                value, cnt = a[0]
                
                if cnt <= k:
                    ans += value*cnt
                    k -= cnt
                    a.popleft()
                else:
                    ans += value * k
                    a[0] = (value, cnt-k)
                    k = 0
            
            print(ans)


if __name__ == '__main__':
    main()
