import random

# Parameters for the test case
N = 500000  # Length of arrays A and B (maximal size)
Q = 500000  # Number of queries (maximal size)

# Construct arrays A and B
# A will contain a repeated pattern of small numbers with some noise
# B will contain a shuffled version of A to break order-based comparisons

pattern = [2, 3, 5, 7]  # Small prime numbers for the base pattern
A = (pattern * (N // len(pattern)))[:N]  # Repeat the pattern to fill N elements
B = A.copy()
random.shuffle(B)  # Shuffle B to make it a valid permutation of A

# Construct queries (l, r, L, R)
queries = []
for _ in range(Q):
    l = random.randint(1, N // 2)  # Random start in the first half of A
    r = random.randint(l, l + N // 100)  # Small range for r to keep overlap low
    L = random.randint(1, N // 2)  # Random start in the first half of B
    R = random.randint(L, L + N // 100)  # Small range for R
    r = min(r, N)  # Ensure r does not exceed N
    R = min(R, N)  # Ensure R does not exceed N
    queries.append((l, r, L, R))

# Output the test case in the required format
output = f"{N} {Q}\n"
output += " ".join(map(str, A)) + "\n"
output += " ".join(map(str, B)) + "\n"
output += "\n".join(f"{l} {r} {L} {R}" for l, r, L, R in queries)

print(output, end="")
