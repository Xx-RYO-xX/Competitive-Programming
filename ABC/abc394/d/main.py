import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()

    stack = []
    pair = {')': '(', ']': '[', '>': '<'}

    other = "([<"
    for S in s:
        if S in other:
            stack.append(S)
        else:
            if not stack or stack[-1] != pair[S]:
                print("No")
                return
            stack.pop()

    print("Yes" if len(stack) == 0 else "No")


if __name__ == '__main__':
    sys.exit(main())
