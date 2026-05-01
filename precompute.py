import sys
import os
import pickle

CACHE_FILE = "cashe.pkl"


def precompute():
    nums = []

    with open(CACHE_FILE, "wb") as f:
        pickle.dump(nums, f)


def input():
    return sys.stdin.readline().rstrip()


def main():
    k = int(input())

    with open(CACHE_FILE, "rb") as f:
        nums = pickle.load(f)

    print(nums[k])


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[-1] == "ONLINE_JUDGE":
        precompute()
    else:
        if not os.path.exists(CACHE_FILE):
            precompute()
        sys.exit(main())
