def main():
    correct = sorted(["H", "2B", "3B", "HR"])
    s = []
    for _ in range(4):
        s.append(input())

    if sorted(s) == correct:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
