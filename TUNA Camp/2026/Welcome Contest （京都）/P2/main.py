from itertools import permutations

path = "test/"
cnt = 0
num = [1, 2, 3, 4]
for ans1 in permutations(num):
    for ans2 in permutations(num):
        for ans3 in permutations(num):
            with open(path + str(cnt), mode="w") as f:
                f.write("".join(str(i) for i in ans1))
                f.write("\n")
                f.write("".join(str(i) for i in ans2))
                f.write("\n")
                f.write("".join(str(i) for i in ans3))
                f.write("\n")
                cnt += 1
