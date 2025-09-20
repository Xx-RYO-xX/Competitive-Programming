import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()

    kenbann = "WBWBWWBWBWBW" * 10

    onkai = {0: "Do", 2: "Re", 4: "Mi", 5: "Fa", 7: "So", 9: "La", 11: "Si"}

    for i in range(len(kenbann)):
        if s == kenbann[i : i + 20]:
            print(onkai[i])
            return


if __name__ == "__main__":
    main()
