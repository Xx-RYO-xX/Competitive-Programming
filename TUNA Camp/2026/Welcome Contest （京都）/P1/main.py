from itertools import permutations

num = [1, 2, 3, 4, 5]
for ans1 in permutations(num):
    for ans2 in permutations(num):
        for ans3 in permutations(num):
            print(*ans1)
            print(*ans2)
            print(*ans3)
            print()
