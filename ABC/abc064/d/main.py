import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()

    stack = []
    for S in s:
        stack.append(S)
        if len(stack) >= 2 and stack[-2] + stack[-1] == "()":

            stack.pop()
            stack.pop()

    print("(" * stack.count(")") + s + ")" * stack.count("("))


if __name__ == "__main__":
    sys.exit(main())
