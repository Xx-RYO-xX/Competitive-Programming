import sys


def yes():
    print("Yes")


def no():
    print("No")


def y_or_n(yes_cond):
    print("Yes" if yes_cond else "No")


def a_to_z():
    return list(chr(ord("a") + i) for i in range(26))


def atcoder():
    return list("atcoder")


def takahashi():
    print("Takahashi")


def aoki():
    print("Aoki")


def readline(back_slash=False):
    if back_slash:
        return sys.stdin.readline()
    else:
        return sys.stdin.readline().rstrip()


def sep_read(types=str):
    if types == str:
        return sys.stdin.readline().rstrip().split()
    else:
        return map(types, sys.stdin.readline().split())


def bit_full_search(lst, n):
    ans = []

    for i in range(2 ** n):
        s_u_m = 0
        for j in range(n):
            bit = (2 ** j)
            if (i // bit) % 2 == 1:
                s_u_m += lst[j]
        ans.append(s_u_m)

    return ans


class Deque:

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
        self.buf[self.tail+1: self.tail+1] = [None] * ex
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

    def __len__(self):
        return (self.tail - self.head) % self.N

    def __getitem__(self, key):
        return self.buf[self.__index(key)]

    def __setitem__(self, key, value):
        self.buf[self.__index(key)] = value

    def __str__(self):
        return 'Deque({0})'.format(str(list(self)))


def main():
    from collections import deque
    from itertools import islice

    sys.setrecursionlimit(10000)

    s = list(readline())

    stack = Deque()
    stack_count = 0
    gomamayo_count = 0

    first_gomamayo = False
    gomamayo = False

    ans = 0

    s_len = len(s)
    for i in range(s_len):
        stack.append(s[i])
        stack_count += 1
        if stack_count >= 2 and stack[-1] == stack[-2]:
            print(stack)
            ans += i

            stack_count = 1
            stack = deque(stack[-1])

            first_gomamayo = True
            gomamayo = True

        if first_gomamayo and not gomamayo:
            ans += 1


    print(ans%998244353)


if __name__ == "__main__":
    main()
